from flask import Flask, jsonify, request, url_for, redirect, session, render_template
# from Templates import form
app = Flask(__name__)
app.config['SECRET_KEY'] = 'somebullshit'
app.config['DEBUG'] = True

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
        # location = request.form['location']

        # return "<h1>Rquest Submitted Successfully </h1>"
        return redirect(url_for('home', name = name))


@app.route('/form', methods = ['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return """<p>
    Got response by {} from {}
    </p>
    """.format(name, location)


if __name__ == "__main__":
    app.run(debug = True)