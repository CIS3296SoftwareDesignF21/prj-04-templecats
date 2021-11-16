from flask import Flask, redirect, url_for, render_template
from flaskext.mysql import MySQL # used to create mysql db connection
app = Flask(__name__)

#Configure the connection to DB
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'jhageman'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Jhageman99?'
app.config['MYSQL_DATABASE_DB'] = 'TempleCats'
mysql.init_app(app)


#define the home page of our site
@app.route('/') # sets the route to the current page
def home():
    
    return render_template("index.html", dexter={"dog":7, "smell":"bad"})  # some basic inline html

@app.route("/<name>")
def user(name):

    lastName = name + '2'
    # create connection to db
    conn = mysql.connect()
    cursor = conn.cursor()
    # insert name into database: first name: name
    # last name: name2
    cursor.execute("INSERT INTO DummyTable(firstName, lastName) VALUES (%s, %s)", (name, lastName))
    cursor.execute("commit")
    # Query database and display results on the page
    sql = "SELECT * FROM DummyTable"
    cursor.execute(sql)
    
    results = cursor.fetchall()
    

    return f"Hello {name}!\n{results}"

# create webpage called admin
@app.route("/admin")
def admin():
    return redirect(url_for('home'))

    # FLASK_APP=tut1.py flask run
