from flask import Flask, render_template, g, request
import sqlite3
from datetime import datetime

app = Flask(__name__, template_folder= "./templates")

#helper functions

def connect_db():
    """
    connects the sqlite database to the application
    """
    sql = sqlite3.connect("./food_log.db")

    # This line of code configures the connection to return rows as sqlite3.Row objects, which provide a convenient way to access the columns of a query result by name.
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    """
        Retrieve the SQLite database connection object.

        This function checks if the connection object exists in the `g` object,
        which is a global object used for storing data during the lifetime of a
        request in a Flask application. If the connection object does not exist,
        it creates a new connection by calling the `connect_db()` function and
        stores it in `g` for future use.

        Returns:
        sqlite3.Connection: The SQLite database connection object.
    """
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """
    Close the database connection after the application context is torn down.

    :param error: The error, if any, that occurred during the request or application context teardown.
    """
    if hasattr(g, "sqlite3"):
        g.sqlite_db.close()


@app.route('/', methods=['POST', 'GET'])
def index():

    db = get_db()
    if request.method == 'POST':
        date = request.form['date']
        datetime_object = datetime.strptime(date, '%Y-%m-%d')
        date_database = datetime.strftime(datetime_object, '%Y%m%d')

        db.execute('insert into log_date (entry_date) values (?)', [date_database])
        db.commit()
    
    cur = db.execute('select entry_date from log_date order by entry_date desc')
    results = cur.fetchall()
    pretty_results = []

    for i in results:
        i_date = {}
        d = datetime.strptime(str(i['entry_date']), '%Y%m%d')
        i_date['entry_date'] = datetime.strftime(d, '%B %d, %Y')
        pretty_results.append(i_date)

    return render_template('home.html', results=pretty_results)

@app.route('/view/<date>') #date format = YYYYMMDD
def view(date):
    db = get_db()
    cur = db.execute('select entry_date from log_date where entry_date = ?', [date])
    result = cur.fetchone()

    d = datetime.strptime(str(result['entry_date']), '%Y%m%d')
    pretty_date = datetime.strftime(d, '%B %m, %Y')


    return  render_template('day.html', date=pretty_date)

@app.route('/food', methods = ['GET', 'POST'])
def food():
    db = get_db()

    if request.method == 'POST':
        name = request.form['name']
        protein = int(request.form['protein'])
        carbohydrate = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])

        calories = protein*4 + carbohydrate*4 + fat*9

        # add into database 
        
        db.execute('insert into food (name, protein, carbohydrates, fats, calories) values (?, ? ,?, ?, ?)', [name, protein, carbohydrate, fat, calories])
        db.commit()

    cur = db.execute('select name, protein, carbohydrates, fats, calories from food')
    results = cur.fetchall()
    
    return render_template('add_food.html', results=results)

if __name__ == '__main__':
    app.run(debug= True, port=8000)