from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/friends')
def frients_list():
    return [{
    "name": "Adil Khan",
    "email": "adil@gamil.com",
    "phone": "067765665656",
    "address": "Guntur",
    "country": "India"
},

{
    "name": "Asif Shaik",
    "email": "asifshaik@gamil.com",
    "phone": "09876546587",
    "address": "Triupathi",
    "country": "India"
},

{
    "name": "Shoyab Shaik",
    "email": "Shoyabsk@gamil.com",
    "phone": "067765665656",
    "address": "Guntur",
    "country": "India"
},

{
    "name": "Aslam Shaik",
    "email": "aslamshaik@gamil.com",
    "phone": "09878766676",
    "address": "Triupathi",
    "country": "India"
}
]