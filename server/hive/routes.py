from flask import render_template, request, jsonify
from hive import app, socketio
from hive.forms import MessageForm
from hive.models import Message
from hive.queries import Query


@app.route("/", methods=["GET", "POST"])
def home():
    form = MessageForm(request.form)
    return render_template("pages/home.html", form=form)

# Sockets


@socketio.on("send message")
def send_message(json, methods=["GET", "POST"]):
    if "message" in json:
        recieved_message = json["message"]
        Query.add_message(recieved_message)


@socketio.on("fetch new message")
def fetch_new_message(methods=["GET", "POST"]):
    row = Query.random_row()
    socketio.emit("send new message to client", row)


@socketio.on("add like")
def add_like(json, methods=["GET", "POST"]):
    msg_id = json["id"]
    Query.add_like(msg_id)
