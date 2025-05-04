import typer

from .info import info
from .server import server

app = typer.Typer()

app.command()(info)
app.command()(server)

if __name__ == "__main__":
    app()
