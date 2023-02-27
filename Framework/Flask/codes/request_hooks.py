from flask import Flask, request, make_response, redirect

app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<p>Bad Request</p>', 400

@app.route('/')
def response_gen():
    response = make_response('<p>This is a cookie!!</p>')
    response.set_cookie('answer', '42')
    return response

@app.route('/red')
def redir():
    return redirect('https://github.com/ppap1771')

if __name__ == '__main__':
    app.run(debug = True)