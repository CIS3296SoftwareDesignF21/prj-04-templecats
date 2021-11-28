from flask import Flask, redirect, url_for, render_template
from flaskext.mysql import MySQL # used to create mysql db connection
app = Flask(__name__, 
        static_url_path='',
        static_folder='static',
        template_folder='static/templates')

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
    return render_template("static/templates/index.html")  # some basic inline html

@app.route('/community_cats')
def community_cats():
    return render_template("static/templates/communitycats.html")

@app.route("/see_cats_outside")
def see_cats_outside():
    return render_template("static/templates/catsoutside.html")

@app.route("/tnr")
def tnr():
    return render_template("static/templates/tnr.html")

@app.route("/our_kitties")
def our_kitties():
   return render_template("static/templates/our_kitties.html")

@app.route("/pet_care")
def pet_care():
   return render_template("static/templates/pet_care.html")

@app.route("/donate_volunteer")
def donate_volunteer():
   return render_template("static/templates/donate_volunteer.html")



# create webpage called admin
@app.route("/admin")
def admin():
    return redirect(url_for('home'))

    # FLASK_APP=tut1.py flask run


if __name__ == '__main__':
    app.run()
