# all the pynote page commands
import typer

app = typer.Typer()


@app.command()
def create(page_name: str, checklist: bool = typer.Option(False)) -> None:
    if checklist:
        print(f"Creating {page_name} as a checklist")

    else:
        print(f"Creating {page_name} as a page")


@app.command()
def delete(page_name: str) -> None:
    print(f"Deleting page {page_name}")


@app.command()
def rename(page_name: str, new_name: str) -> None:
    print("Renaming page")


@app.command(name="list")
def list_pages() -> None:
    print("Listing notes")


@app.command()
def show(page_name: str) -> None:
    print("Show Page")


@app.command()
def edit(page_name: str) -> None:
    print("Edit page")
