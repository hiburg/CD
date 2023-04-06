from flask import Flask

#comment
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is the CD assignment !@!@!@'
