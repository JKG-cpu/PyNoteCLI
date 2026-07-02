import typer

from .commands import config_app, page_app

app = typer.Typer()

# Add different sub commands
app.add_typer(config_app, name = "config")
app.add_typer(page_app, name = "page")

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print("Opening TUI")

@app.command()
def tui() -> None:
    print("Opening TUI")
