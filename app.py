from flask import Flask, request, json

from logic_application.database import push_database, update_user_state
from settings import *
import messageHandler

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello from Flask!"


@app.route(config['app']['tg']['posturi'], methods=["POST"])
def telegram():
    data = json.loads(request.data)
    if data.get("message"):
        branch_name, status = push_database(data["message"])
        branch_name, status = messageHandler.create_answer(
            data["message"], config['app']['tg']['token'],
            branch_name, str(status),
        )
        update_user_state(
            branch=branch_name,
            status=status,
            user_id=data["message"]["chat"]["id"]
        )
        return "ok"
    return "nothing"


app.run(config['app']['host'], config['app']['port'])
