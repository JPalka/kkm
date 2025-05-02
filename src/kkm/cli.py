import typer

from .info import info


app = typer.Typer()

app.command()(info)

@app.command()
def server():
    print("Starting kkm info server")


if __name__ == "__main__":
    app()
