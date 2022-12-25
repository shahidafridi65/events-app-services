from flask import Flask
import json

app = Flask(__name__)

friends = [];
with open('friends.json','r') as f:
    friends = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/friends')
def frients_list():
    return friends

@app.route('/api/friends/<int:id>')
def get_friend(id):
    friend = {}
    for f in friends:
        if f.get("id") == id:
            friend = f
    return friend