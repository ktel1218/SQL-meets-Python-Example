from flask import Flask, request, render_template, url_for
import jinja2

import sqlite3

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index():

    connection = sqlite3.connect('melons.db')
    cursor = connection.cursor()
    # print CURSOR.execute("SELECT * FROM melons").fetchall()

    melons = []
    if 'submitted' in request.form:
        print request.form
        min_price = request.form.get('min')
        max_price = request.form.get('max')
        if min_price and max_price:
            query = """
            SELECT * 
            FROM melons 
            WHERE price > ? 
                AND price < ?
            """
            melons = CURSOR.execute(query, (int(min_price), int(max_price))).fetchall()

    return render_template("index.html", melons = melons)

if __name__ == "__main__":
    app.run(debug=True, port=5000)