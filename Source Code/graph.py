from langgraph.graph import StateGraph, START, END

from state import CustomerState
from nodes import (
    classify_intent,
    sales_agent,
    technical_agent,
    billing_agent,
    account_agent,
    memory_node,
    approval_node,
    human_approval_node,
    supervisor_node
)

builder = StateGraph(CustomerState)

# Nodes
builder.add_node("classifier", classify_intent)
builder.add_node("sales", sales_agent)
builder.add_node("technical", technical_agent)
builder.add_node("billing", billing_agent)
builder.add_node("account", account_agent)
builder.add_node("memory", memory_node)
builder.add_node("approval", approval_node)
builder.add_node("human_approval", human_approval_node)
builder.add_node("supervisor", supervisor_node)

# START
builder.add_edge(START, "classifier")


# ROUTING
def route_department(state):
    return state["department"]


builder.add_conditional_edges(
    "classifier",
    route_department,
    {
        "sales": "sales",
        "technical": "technical",
        "billing": "billing",
        "account": "account",
        "memory": "memory"
    }
)

# Memory ends directly
builder.add_edge("memory", END)

# Normal flow → approval
builder.add_edge("sales", "approval")
builder.add_edge("technical", "approval")
builder.add_edge("billing", "approval")
builder.add_edge("account", "approval")

# Approval flow
builder.add_edge("approval", "human_approval")
builder.add_edge("human_approval", "supervisor")
builder.add_edge("supervisor", END)

graph = builder.compile()