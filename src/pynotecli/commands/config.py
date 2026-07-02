# all the pynote config commands
import typer

app = typer.Typer()

@app.command()
def show() -> None:
    print("Show config settings")

@app.command()
def edit() -> None:
    print("Edit config settings")

@app.command()
def reset() -> None:
    print("Reset config settings")
