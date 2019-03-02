from wtforms import Form, StringField, validators


class MessageForm(Form):
    message = StringField("Message", [validators.Length(min=4)])
