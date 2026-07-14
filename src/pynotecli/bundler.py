import typer

from .commands import config_app, page_app, note_app
from .core import setup, clear_data, Text

app = typer.Typer()

# Add different sub commands
app.add_typer(config_app, name="config")
app.add_typer(page_app, name="page")
app.add_typer(note_app, name="note")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print("Opening TUI")


@app.command()
def tui() -> None:
    print("Opening TUI")


@app.command(name="setup")
def stp() -> None:
    setup()


@app.command()
def clear() -> None:
    user_input = Text.warning(
        "Are you sure you want to clear all data (Y/N)?", is_input=True
    )

    if user_input:
        if user_input.lower() == "y" or user_input.lower().startswith("y"):
            clear_data()

        else:
            return

    else:
        Text.info("User input not caught, exitting...")
