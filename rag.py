from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

files = [
    "documents/company_policy.txt",
    "documents/pricing_guide.txt",
    "documents/technical_manual.txt",
    "documents/faq.txt"
]

docs = []

for file in files:
    loader = TextLoader(file, encoding="utf-8")
    docs.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="vectorstore"
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 1}      
)


def retrieve_context(query):
    docs = retriever.invoke(query)

    if not docs:
        return "No relevant information found."

    return docs[0].page_content.strip()