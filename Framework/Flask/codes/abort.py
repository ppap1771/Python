from flask import Flask, abort

app = Flask(__name__)
def load_user(id):
    return 1
    
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, </h1>' 

if __name__ == '__main__':
    app.run(debug = True)
