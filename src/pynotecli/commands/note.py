import typer

from ..core import add_note, delete_note, edit_note, list_notes

app = typer.Typer()


@app.command()
def add(
    name: str,
    desc: str = typer.Option(default=None),
    page: str = typer.Option(default=None),
):
    add_note(name=name, desc=desc, page=page)


@app.command()
def edit(name: str, page: str = typer.Option(default=None)):
    edit_note(name=name, page=page)


@app.command()
def delete(name: str, page: str = typer.Option(default=None)):
    delete_note(name=name, page=page)


@app.command(name="list")
def ls(page: str = typer.Option(default=None)):
    list_notes(page=page)
