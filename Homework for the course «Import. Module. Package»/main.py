
import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
from rich.console import Console

console = Console()
console.print(f"[bold yellow]Дата:[/bold yellow] {datetime.datetime.now().strftime('%Y-%m-%d')}")

if __name__ == '__main__':
    console.rule("[yellow]Выполняются операции[/yellow]")
    calculate_salary()
    get_employees()
    console.rule("[yellow]Операции завершены[/yellow]")