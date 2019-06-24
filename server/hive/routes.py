from flask import jsonify
from hive import app, socketio
from hive.models import Message
from hive.queries import Query

# dummy route


@app.route("/ping", methods=["GET", "POST"])
def home():
    return jsonify("pong")

# Sockets


@socketio.on("send_msg")
def send_msg(json, methods=["GET", "POST"]):
    if "msg" in json:
        recieved_msg = json["msg"]
        print(recieved_msg)


@socketio.on("fetch_new_msg")
def fetch_new_msg(methods=["GET", "POST"]):
    try:
        row = Query.random_row()
        print(row)
        socketio.emit("msg_to_client", row)
    except AttributeError as e:
        print(f"{e}")


@socketio.on("add_like")
def add_like(json, methods=["GET", "POST"]):
    msg_id = json["id"]
    Query.add_like(msg_id)


@socketio.on("add_report")
def add_report(json, methods=["GET", "POST"]):
    msg_id = json["id"]
    Query.add_report(msg_id)


def update_stats(msg_id):
    stats = Query.get_stats(msg_id)
    socketio.emit("update_stats", )
# update parameters, likes; reports etc
