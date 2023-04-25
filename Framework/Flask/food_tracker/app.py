from flask import Flask, render_template, g, request
import sqlite3

app = Flask(__name__, template_folder= "./templates")

#helper functions
def connect_db():
    sql = sqlite3.connect("/media/ayush/personal space/langs/Python/Framework/Flask/food_tracker/food_log.db")
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
    return render_template('home.html')

@app.route('/view')
def view():
    return  render_template('day.html')

@app.route('/food', methods = ['GET', 'POST'])
def food():
    if request.method == 'POST':
        name = request.form['name']
        protien = int(request.form['protein'])
        carbohydrate = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])

        calories = protien*4 + carbohydrate*4 + fat*9

        # add into database 
        db = get_db()
        db.execute('insert into food (name, protein, carbohydrates, fats, calories) values (?, ? ,?, ?, ?)', [name, protien, carbohydrate, fat, calories])
        db.commit()
    return render_template('add_food.html')

if __name__ == '__main__':
    app.run(debug= True)