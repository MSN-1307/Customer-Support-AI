from rag import retrieve_context
from memory import recall_memory


# ---------------- INTENT CLASSIFIER ----------------

def classify_intent(state):

    query = state["query"].lower()

    if "previous" in query:
        department = "memory"

    elif any(word in query for word in
             ["refund", "payment", "invoice",
              "cancel", "compensation", "management"]):
        department = "billing"

    elif any(word in query for word in
             ["password", "profile", "account"]):
        department = "account"

    elif any(word in query for word in
             ["error", "crash", "login",
              "install", "configuration", "upload"]):
        department = "technical"

    elif any(word in query for word in
             ["price", "pricing", "plan", "subscription"]):
        department = "sales"

    else:
        department = "sales"

    state["department"] = department
    return state


# ---------------- SALES ----------------

def sales_agent(state):

    context = retrieve_context(state["query"])

    state["retrieved_context"] = context

    state["response"] = (
        f"Dear {state['customer_name']},\n\n"
        "Based on our Pricing Guide, here are the available subscription plans:\n\n"
        f"{context}\n\n"
        "If you'd like help choosing the best plan, we'd be happy to assist."
    )

    return state


# ---------------- TECHNICAL ----------------

def technical_agent(state):

    context = retrieve_context(state["query"])

    state["retrieved_context"] = context

    state["response"] = (
        f"Dear {state['customer_name']},\n\n"
        "Based on our Technical Manual, please follow the instructions below:\n\n"
        f"{context}\n\n"
        "If the issue persists, please contact our Technical Support team."
    )

    return state


# ---------------- BILLING ----------------

def billing_agent(state):

    context = retrieve_context(state["query"])

    state["retrieved_context"] = context

    state["response"] = (
        f"Dear {state['customer_name']},\n\n"
        "According to our Company Policy:\n\n"
        f"{context}\n\n"
        "If your request requires approval, our support team will process it shortly."
    )

    return state


# ---------------- ACCOUNT ----------------

def account_agent(state):

    context = retrieve_context(state["query"])

    state["retrieved_context"] = context

    state["response"] = (
        f"Dear {state['customer_name']},\n\n"
        "Based on our FAQ document:\n\n"
        f"{context}\n\n"
        "Please let us know if you need any further assistance."
    )

    return state


# ---------------- MEMORY ----------------

def memory_node(state):

    state["retrieved_context"] = "Conversation retrieved from SQLite memory."

    state["response"] = (
        f"Dear {state['customer_name']},\n\n"
        "Your previous support issue was:\n\n"
        + recall_memory()
    )

    return state


# ---------------- APPROVAL ----------------

def approval_node(state):

    query = state["query"].lower()

    risky = [
        "refund",
        "cancel",
        "closure",
        "compensation",
        "management"
    ]

    state["approval_required"] = any(
        word in query for word in risky
    )

    return state


# ---------------- HUMAN APPROVAL ----------------

def human_approval_node(state):

    if state["approval_required"]:

        print("\nHuman Approval Required")

        decision = input("Approve request? (yes/no): ").strip().lower()

        if decision == "yes":
            state["approved"] = True

        else:
            state["approved"] = False
            state["response"] = (
                "Your request has not been approved by the supervisor."
            )

    else:
        state["approved"] = True

    return state


# ---------------- SUPERVISOR ----------------

def supervisor_node(state):

    if state["approved"]:

        state["response"] += (
            "\n\nThank you for contacting ABC Technologies AI Customer Support."
        )

    else:

        state["response"] = (
            "Final response could not be generated because the request was not approved."
        )

    return state