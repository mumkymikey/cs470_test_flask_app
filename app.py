from flask import Flask, render_template, jsonify, request
import pymysql
import yaml

# create instance of Flask class
app = Flask(__name__)

# reads database.yml and configures mysql connection
with open("database.yml", "r") as stream:
    try:
        db_config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

mysql = pymysql.connect(
    host = db_config['MYSQL_HOST'],
    user = db_config['MYSQL_USER'],
    password = db_config['MYSQL_PASSWORD'],
    db = db_config['MYSQL_DB'],
    )

# base endpoint that renders world map UI
@app.route('/')
def index():
    return render_template('world.html')

# POST endpoint used for receiving country name on click.
# the country name is used to fetch general info on clicked country.
@app.route('/countrymethod', methods=["POST"])
def post_country_javascript():
    cursor = mysql.cursor()
    country_name = request.form["countryData"]

    cursor.execute("SELECT * FROM country WHERE name = " + country_name)
    country_info = cursor.fetchall()
    cursor.close()

    print(country_info)
    return 'OK'
