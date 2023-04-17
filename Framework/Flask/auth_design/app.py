from flask import Flask, jsonify, request, url_for, redirect, session, render_template

app = Flask(__name__)
# app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug = True)