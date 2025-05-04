import datetime
from flask import Flask, request, jsonify
import typer
from typing_extensions import Annotated

from .api import Api

server_app = Flask(__name__)

@server_app.route("/")
def hello_world():
    data = {'data': 'hello world'}
    return data

@server_app.route("/client/<client_number>/tickets")
def tickets_index(client_number):
    date = request.args.get('date', datetime.datetime.today().strftime("%Y-%m-%d"))
    x = Api(client_number, date, {'debug': False})
    tickets = x.get_tickets()
    data = tickets
    return jsonify(data)

@server_app.route("/client/<client_number>/tickets/latest")
def tickets_latest(client_number):
    date = request.args.get('date', datetime.datetime.today().strftime("%Y-%m-%d"))
    x = Api(client_number, date, {'debug': False})
    tickets = x.get_tickets()
    data = tickets[-1]
    return jsonify(data)

def server(
    port: Annotated[str, typer.Option(help="Port to run server on(default 5000)")] = "5000",
    debug: Annotated[bool, typer.Option(help="Run server in debug mode")] = False,
):
    print("Starting kkm server: ")
    server_app.run(debug=debug)
