# AI-Powered Customer Support Automation System using LangGraph

## Project Overview

The AI-Powered Customer Support Automation System is a multi-agent customer service application developed using **LangGraph**, **LangChain**, **ChromaDB**, and **SQLite Memory**.

The system automates customer support by identifying customer intent, routing requests to the appropriate department, retrieving relevant information from company documents using Retrieval-Augmented Generation (RAG), maintaining conversation history, handling high-risk requests through Human-in-the-Loop approval, and generating professional customer responses.

This project demonstrates how multiple AI agents can collaborate using LangGraph workflows to automate real-world customer support processes.

---

# Features

- Customer query processing
- Intent classification
- Multi-agent workflow using LangGraph
- Department-based routing
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Store
- SQLite conversation memory
- Human-in-the-Loop approval
- Supervisor validation
- Professional terminal interface using Rich
- Modular project architecture

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangGraph | Workflow orchestration |
| LangChain | AI application framework |
| ChromaDB | Vector database |
| HuggingFace Embeddings | Document embeddings |
| Sentence Transformers | Semantic search |
| SQLite | Conversation memory |
| Rich | Terminal UI |
| VS Code | Development Environment |

---

# Project Structure

```
customer_support_ai/
│
├── app.py
├── graph.py
├── state.py
├── nodes.py
├── rag.py
├── memory.py
├── supervisor.py
│
├── documents/
│   ├── company_policy.txt
│   ├── pricing_guide.txt
│   ├── technical_manual.txt
│   └── faq.txt
│
├── vectorstore/
│
├── database/
│   └── memory.db
│
├── workflow_diagram.png
├── README.md
└── requirements.txt
```

---

# System Workflow

1. Customer submits a support query.
2. Intent Classifier identifies the query type.
3. LangGraph routes the query to the appropriate support department.
4. RAG retrieves relevant information from company documents.
5. Department agent generates a response.
6. High-risk requests are sent for Human Approval.
7. Supervisor validates the response.
8. Conversation is stored in SQLite memory.
9. Final response is displayed to the customer.

---

# Support Departments

## Sales

Handles:

- Product Information
- Pricing Plans
- Subscription Details

Knowledge Source:

- Pricing Guide

---

## Technical Support

Handles:

- Application Errors
- Login Problems
- Installation Issues
- Configuration Problems

Knowledge Source:

- Technical Manual

---

## Billing

Handles:

- Payments
- Refund Requests
- Invoices
- Subscription Cancellation

Knowledge Source:

- Company Policy Document

---

## Account

Handles:

- Password Reset
- Profile Updates
- Account Activation
- Account Deactivation

Knowledge Source:

- FAQ Document

---

# Knowledge Base Documents

The system retrieves information using Retrieval-Augmented Generation (RAG) from the following documents:

- Company Policy Document
- Pricing Guide
- Technical Manual
- FAQ Document

These documents are converted into embeddings using HuggingFace Sentence Transformers and stored inside ChromaDB.

---

# Human-in-the-Loop

The following requests require manual approval before a response is sent:

- Refund Request
- Subscription Cancellation
- Account Closure
- Compensation Request
- Escalation to Management

If any of these requests are detected, the system pauses execution and asks the supervisor for approval.

Example:

```
Human Approval Required

Approve request? (yes/no)
```

---

# SQLite Memory

The system stores customer interactions inside SQLite.

Example:

Customer:

```
My name is David.
I have a billing issue.
```

Later:

```
What was my previous support issue?
```

The system retrieves the previous interaction directly from SQLite memory.

---

# LangGraph Workflow

The workflow consists of the following nodes:

- Intent Classifier
- Sales Agent
- Technical Agent
- Billing Agent
- Account Agent
- Memory Node
- Approval Node
- Human Approval Node
- Supervisor Node

Conditional routing is implemented using LangGraph.

---

# Retrieval-Augmented Generation (RAG)

The RAG pipeline consists of:

Customer Query

↓

HuggingFace Embeddings

↓

ChromaDB Vector Search

↓

Relevant Document Retrieval

↓

Department Agent

↓

Final Response

The retrieved document context is displayed separately before generating the final response.

---

# Installation

## Clone the repository

```bash
git clone https://github.com/yourusername/customer_support_ai.git

cd customer_support_ai
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Project

```bash
python app.py
```

---

# Demonstration Queries

## Query 1

```
What are the pricing plans available for your software?
```

Expected Department

Sales

---

## Query 2

```
I forgot my account password.
```

Expected Department

Account

---

## Query 3

```
My application crashes whenever I upload a file.
```

Expected Department

Technical Support

---

## Query 4

```
I need a refund for my annual subscription.
```

Expected Department

Billing

Human Approval Required

---

## Query 5

```
What was my previous support issue?
```

Expected Output

SQLite Memory Recall

---

# Project Deliverables

- LangGraph Workflow
- Source Code
- RAG Integration
- SQLite Memory
- Human Approval Workflow
- Supervisor Agent
- README Documentation
- Workflow Diagram
- Execution Screenshots

---

# Assignment Tasks Covered

| Task | Status |
|-------|--------|
| Workflow Design | Completed |
| State Design | Completed |
| Intent Classification | Completed |
| Conditional Routing | Completed |
| Department Agents | Completed |
| RAG Integration | Completed |
| SQLite Memory | Completed |
| Human-in-the-Loop | Completed |
| Supervisor Agent | Completed |
| Demonstration | Completed |

---

# Future Improvements

- Replace rule-based intent classification with LLM-based classification.
- Integrate Qwen or Llama using Ollama.
- Add Streamlit web interface.
- Enable multi-user support.
- Store customer profiles in a relational database.
- Deploy on cloud infrastructure.
- Integrate real company documents.
- Add authentication and role-based access.

---

# Conclusion

This project demonstrates an end-to-end AI-powered customer support automation system using LangGraph. It combines multi-agent workflows, Retrieval-Augmented Generation, SQLite memory, and Human-in-the-Loop approval to automate customer service while ensuring critical requests receive human supervision.

The modular architecture makes the system scalable and suitable for extending into production-grade AI customer support applications.

---

## Developed For

AI-Powered Customer Support Automation System using LangGraph

Academic Project

ABC Technologies