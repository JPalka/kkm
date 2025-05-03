import datetime
import os

import typer
from typing_extensions import Annotated

from .api import Api

def info(
    client_number: Annotated[str, typer.Argument(help="Client number on KKM card")],
    date: Annotated[str, typer.Option(help="Date to check in format YYYY-MM-DD(defaults to today)")] = datetime.datetime.today().strftime("%Y-%m-%d"),
    short: Annotated[bool, typer.Option(help="Just print if card is active today")] = False,
    debug: Annotated[bool, typer.Option(help="Print debug info")] = False,
    notify: Annotated[str, typer.Option(help="Send system notification. For use in other scripts using this.")] = "0",
):
    if debug == True:
        print(f"Printing info abount client tickets: {client_number} for {date}")
    x = Api(client_number, date, {'debug': debug})
    tickets = x.get_tickets()
    if tickets == []:
        print("No ticket")
        if notify:
            os.system('No ticket')  
    else:
        expires_at = tickets[-1].expires_at
        print(f"Ticket active until: {expires_at}")
        if notify:
            os.system(f'notify-send "Ticket active until: {expires_at}"')  
