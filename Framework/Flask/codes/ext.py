from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@manager.route('/')
def index():
    return "<p>Hello</p>"

if __name__ == "__main__" :
    manager.run()