import os, time
from flask import Flask, render_template, request, url_for
from collections import deque
from flask_socketio import emit, SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

USERS = {}
CHANNELS = {"Public": {"messages": deque([], maxlen=100), "username": "default"}}    


@app.route('/', methods = ['GET', 'POST'])
def index() : 
    name = ""
    if request.method == 'POST' :
        if request.form['displayName'] != "" : 
            name = request.form['displayName']
            return render_template('home.html', name = name)
        if request.form['name'] != "":
            channelname = request.form['name']
            return render_template('home.html', channelname = channelname)
    return render_template('displayName.html')



if __name__=='__main__' :
    app.run(debug=True)