from rich.console import Console

__all__ = ["Text"]


class Text:
    console = Console()

    @staticmethod
    def text(text: str):
        Text.console.print(f"[bold white]{text}[/bold white]")

    @staticmethod
    def error(text: str):
        Text.console.print(f"[bold red]{text}[/bold red]")

    @staticmethod
    def success(text: str):
        Text.console.print(f"[bold green]{text}[/bold green]")

    @staticmethod
    def info(text: str):
        Text.console.print(f"[bold cyan]{text}[/bold cyan]")
