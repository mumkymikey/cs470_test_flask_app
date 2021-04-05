from flask import Flask, render_template
import pymysql

app = Flask(__name__)

mysql = pymysql.connect(
    host = 'cs470-project.cpmlwhtijlwu.us-east-2.rds.amazonaws.com',
    user = 'admin',
    password = 'Kz3kD0in8nzRceRam2BQ',
    db = 'cs470_countries',
    )

@app.route('/')
def index():
    cursor = mysql.cursor()

    # gets all countries
    cursor.execute('''SELECT * FROM country''')
    countries = cursor.fetchall()
    cursor.close()

    return render_template('index.html', countries=countries)
