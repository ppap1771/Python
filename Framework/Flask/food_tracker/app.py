from flask import Flask, render_template, g, request
from datetime import datetime
from database import get_db, connect_db

app = Flask(__name__, template_folder= "./templates")

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
    """
        Renders the home page with date entries and nutritional information.

        Retrieves data from the database, including the date entries and corresponding nutritional information 
        (protein, carbohydrates, fats, and calories) for each entry. Converts the entry dates into a human-readable 
        format. Renders the home.html template with the retrieved data to display on the home page.

        Returns:
            rendered template (HTML): The rendered home.html template with the date entries and nutritional information.
    """
    db = get_db()
    if request.method == 'POST':
        date = request.form['date']
        datetime_object = datetime.strptime(date, '%Y-%m-%d')
        date_database = datetime.strftime(datetime_object, '%Y%m%d')

        db.execute('insert into log_date (entry_date) values (?)', [date_database])
        db.commit()
    
    cur = db.execute('''select log_date.entry_date, sum(food.protein) as protein, sum(food.carbohydrates) as carbohydrates, 
                        sum(food.fats) as fats, sum(food.calories) as calories from log_date 
                        join food_logs on food_logs.log_date_id = log_date.id 
                        join food on food.id = food_logs.food_id group by log_date.id order by log_date.entry_date desc''')
    results = cur.fetchall()
    date_results = []

    for i in results:
        i_date = {}
        i_date['entry_date'] = i['entry_date']
        i_date['protein'] = i['protein']
        i_date['carbohydrates'] = i['carbohydrates']
        i_date['fats'] = i['fats']
        i_date['calories'] = i['calories']
        d = datetime.strptime(str(i['entry_date']), '%Y%m%d')
        i_date['pretty_date'] = datetime.strftime(d, '%B %d, %Y')
        date_results.append(i_date)

    return render_template('home.html', results=date_results)

@app.route('/view/<date>', methods=['POST', 'GET']) #date format = YYYYMMDD
def view(date):
    """
        Handles the '/view/<date>' route for viewing and logging food items.

        Args:
            date (str): The date in the format YYYYMMDD.

        Returns:
            str: The rendered HTML template for displaying food items and log information.

        Methods:
            - GET: Retrieves the log information and renders the template for the specified date.
            - POST: Inserts a new food log entry into the database for the specified date.
    """
    
    db = get_db()
    cur = db.execute('select id, entry_date from log_date where entry_date = ?', [date])
    date_result = cur.fetchone()

    if request.method == 'POST':
        # return '<h1>The food item is #{}</h1>'.format(request.form['food_select'])
        db.execute('insert into food_logs (food_id, log_date_id) values (?, ?)', 
                   [int(request.form['food-select']), int(date_result['id'])])
        db.commit()
    
    

    d = datetime.strptime(str(date_result['entry_date']), '%Y%m%d')
    pretty_date = datetime.strftime(d, '%B %d, %Y')
    food_cur = db.execute('select id, name from food')
    food_results = food_cur.fetchall()

    log_cur = db.execute('''select food.name, food.protein, food.carbohydrates, food.fats, food.calories 
                            from log_date join food_logs on food_logs.log_date_id = log_date.id 
                            join food on food.id = food_logs.food_id 
                            where log_date.entry_date = ?''', [date])

    log_results = log_cur.fetchall()

    totals = {}
    totals['protein'] = 0
    totals['carbohydrates'] = 0
    totals['fats'] = 0
    totals['calories'] = 0

    for food in log_results:
        totals['protein'] += food['protein']
        totals['carbohydrates'] += food['carbohydrates']
        totals['fats'] += food['fats']
        totals['calories'] += food['calories']

    return  render_template('day.html', entry_date=date_result['entry_date'], pretty_date=pretty_date, \
                            food_results=food_results, log_results=log_results, totals=totals)

@app.route('/food', methods = ['GET', 'POST'])
def food():
    """
        Renders the add_food.html template and handles the addition of food items.

        If the request method is POST, extracts the food item details (name, protein, carbohydrates, fat) from the 
        request form and calculates the calorie value based on the provided nutrient values. Inserts the food item 
        and its details into the database. 

        Retrieves all food items from the database and renders the add_food.html template, passing the retrieved 
        food items to display in the template.

        Returns:
            rendered template (HTML): The rendered add_food.html template with the retrieved food items.
    """
    db = get_db()

    if request.method == 'POST':
        name = request.form['name']
        protein = int(request.form['protein'])
        carbohydrate = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])

        calories = protein*4 + carbohydrate*4 + fat*9

        # add into database 
        
        db.execute('insert into food (name, protein, carbohydrates, fats, calories) values (?, ? ,?, ?, ?)', 
                   [name, protein, carbohydrate, fat, calories])
        db.commit()

    cur = db.execute('select name, protein, carbohydrates, fats, calories from food')
    results = cur.fetchall()
    
    return render_template('add_food.html', results=results)

if __name__ == '__main__':
    app.run(debug= True, port=8000)