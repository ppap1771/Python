from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g
import sqlite3
# from Templates import form
app = Flask(__name__, template_folder='./template')
app.config['SECRET_KEY'] = 'somebullshit'
app.config['DEBUG'] = True

def connect_db():
    sql = sqlite3.connect("/media/ayush/personal space/langs/Python/Framework/Flask/db/data.db")
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "sqlite3"):
        g.sqlite_db.close()

@app.route('/')
def index():
    return "<h1>FFFFFFFF</h1>"

@app.route('/home/<string:name>', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'], defaults = {'name' : 'Default'}) 
def home(name): 
    session['name'] = name
    return render_template('home.html', name = name, display = True)

@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = 'notinSession!!'
    return jsonify({'key1' : 'value', 'key2' : [1, 2, 3], 'name' : name })

@app.route('/query')
def query():
    name = request.args.get('name')
    loc = request.args.get('location')
    return '<h1>You are at the query page</h1> \n name = {} \n loc = {}'.format(name, loc)

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        location = request.form['location']
        db = get_db()
        db.execute('insert into users (name, location) values (?, ?)', [name, location])
        db.commit()
        # return "<h1>Rquest Submitted Successfully </h1>"
        return redirect(url_for('home', name = name))


@app.route('/form', methods = ['POST'])
def process():
    name = request.form['name']
    # location = request.form['location']
    return """<p>
    Got response by {} from {}
    </p>
    """.format(name, location)

@app.route('/getresults')
def get_results():
    db = get_db()
    cur = db.execute('select id, name, location from users')
    result = cur.fetchall()
    return "<h1>Your name: {}, Your location: {}</h1>".format(result[1]['name'], result[1]['location'])

if __name__ == "__main__":
    app.run(debug = True)