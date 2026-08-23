from graph import graph
from memory import save_memory

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

console.print(
    Panel.fit(
        "[bold cyan]ABC Technologies[/bold cyan]\n"
        "[bold green]AI Customer Support System[/bold green]\n\n"
        "[yellow]Type 'exit' anytime to close the application.[/yellow]",
        title="Welcome",
        border_style="bright_blue",
    )
)

customer_name = console.input(
    "[bold yellow]Enter Customer Name:[/bold yellow] "
)

while True:

    query = console.input(
        "\n[bold yellow]Enter your query:[/bold yellow] "
    )

    if query.lower() == "exit":
        console.print(
            "\n[bold green]Thank you for using ABC Technologies AI Customer Support![/bold green]"
        )
        break

    state = {
        "customer_name": customer_name,
        "query": query,
        "department": "",
        "retrieved_context": "",
        "approval_required": False,
        "approved": False,
        "response": "",
        "history": []
    }

    result = graph.invoke(state)

    save_memory(
        result["query"],
        result["response"]
    )

    # -------- Decide Knowledge Source --------

    dept = result["department"].lower()

    if dept == "sales":
        source = "Pricing Guide"

    elif dept == "technical":
        source = "Technical Manual"

    elif dept == "billing":
        source = "Company Policy Document"

    elif dept == "account":
        source = "FAQ Document"

    elif dept == "memory":
        source = "SQLite Conversation Memory"

    else:
        source = "Knowledge Base"

    # -------- Summary Table --------

    table = Table(
        title="Support Summary",
        box=box.ROUNDED,
        header_style="bold cyan"
    )

    table.add_column("Field", style="cyan", width=25)
    table.add_column("Value", style="green")

    table.add_row("Customer", result["customer_name"])
    table.add_row("Department", result["department"].title())
    table.add_row(
        "Approval Required",
        "Yes" if result["approval_required"] else "No"
    )
    table.add_row(
        "Approved",
        "Yes" if result["approved"] else "No"
    )
    table.add_row("Knowledge Source", source)

    console.print()
    console.print(table)

    # -------- Retrieved Context --------

    console.print(
        Panel(
            f"[bold cyan]Source:[/bold cyan] {source}\n\n"
            f"{result['retrieved_context']}",
            title="Retrieved Context (RAG)",
            border_style="bright_blue"
        )
    )

    # -------- Final Response --------

    console.print(
        Panel(
            result["response"],
            title="Final Response",
            border_style="green"
        )
    )