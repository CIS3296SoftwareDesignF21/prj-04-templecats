from flask import Flask, redirect, url_for, render_template, request
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
    return render_template("index.html")  # some basic inline html

@app.route('/communitycats')
def community_cats():
    return render_template("communitycats.html")

@app.route("/catsoutside")
def see_cats_outside():
    return render_template("catsoutside.html")

@app.route("/tnr")
def tnr():
    return render_template("tnr.html")

@app.route("/our_kitties")
def our_kitties():
   return render_template("our_kitties.html")

@app.route("/pet_care")
def pet_care():
   return render_template("pet_care.html")

@app.route("/donate_volunteer",methods=['GET','POST'])
def donate_volunteer():
    # Handle adding user form entry to database
    if request.method=='POST':
        first_name=request.form['fname']
        last_name=request.form['lname']
        email_id=request.form['emailid']
        address_id=request.form['addressid']
        phone_id=request.form['phoneid']
        connection = mysql.get_db()
        cursor = connection.cursor()
        query="INSERT INTO volunteer_data(first_name,last_name,email, address, phone) VALUES(%s,%s,%s,%s,%s)"
        cursor.execute(query,(first_name,last_name,email_id, address_id, phone_id))
        connection.commit()
    #render html
    return render_template("donate_volunteer.html")



if __name__ == '__main__':
    app.run()
