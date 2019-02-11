from flask import render_template, request
from hive import app, db, socketio
from hive.forms import MessageForm
from hive.models import Message
from hive.queries import Query
# from hive.nlp import NLP


@app.route("/", methods=["GET", "POST"])
def home():
    form = MessageForm(request.form)
    return render_template("pages/home.html", form=form)

# Sockets


@socketio.on("send message")
def handle_my_custom_event(json, methods=["GET", "POST"]):
    print("----------------------------------")
    if "message" in json:
        recieved_message = json["message"]
        message = Message(message=recieved_message)
        db.session.add(message)
        db.session.commit()


@socketio.on("fetch new message")
def fetch_new_message(methods=["GET", "POST"]):
    message = Query.random_message()
    json = {"message": f"{message}"}
    socketio.emit("send new message to client", json)
