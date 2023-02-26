from flask import Flask, request, current_app

# request.method      # get the request method
app = Flask(__name__)


app.route('/')
def index():
    return '<p> Shit working fine? </p>'

# app_context = app.app_context()
# app_context.push()

# print(current_app.name)    # get the name of the application 
