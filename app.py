from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/friends')
def frients_list():
    with open('friends.json','r') as f:
        All_friends = json.load(f)
        
    return All_friends