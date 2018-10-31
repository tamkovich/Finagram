from flask import Flask, request, json
from settings import *
import messageHandler

app = Flask(__name__)
branch_name, status = None, None


@app.route("/")
def hello_world():
    return "Hello from Flask!"


@app.route(config['app']['tg']['posturi'], methods=["POST"])
def telegram():
    data = json.loads(request.data)
    if data.get("message"):
        global branch_name, status
        branch_name, status = messageHandler.create_answer(
            data["message"], config['app']['tg']['token'],
            branch_name, status,
        )
        return "ok"
    return "nothing"


app.run(config['app']['host'], config['app']['port'])
