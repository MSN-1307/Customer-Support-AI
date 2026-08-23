from typing import TypedDict, List


class CustomerState(TypedDict):
    customer_name: str
    query: str
    department: str
    retrieved_context: str
    approval_required: bool
    approved: bool
    response: str
    history: List[str]