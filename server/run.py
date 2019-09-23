from hive import app, socketio

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True)


# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
