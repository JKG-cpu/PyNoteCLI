from rich.console import Console
from rich.progress import Progress

__all__ = ["Text"]


class Text:
    console = Console()

    @staticmethod
    def text(text: str, style: str = "bold white"):
        Text.console.print(f"[{style}]{text}[/{style}]")

    @staticmethod
    def error(text: str):
        Text.console.print(f"[bold red]{text}[/bold red]")

    @staticmethod
    def success(text: str):
        Text.console.print(f"[bold green]{text}[/bold green]")

    @staticmethod
    def info(text: str):
        Text.console.print(f"[bold cyan]{text}[/bold cyan]")

    @staticmethod
    def progress() -> Progress:
        return Progress(console=Text.console)

    @staticmethod
    def status(text: str, style: str):
        return Text.console.status(f"[{style}]{text}[/{style}]")


CONFIG = {}
