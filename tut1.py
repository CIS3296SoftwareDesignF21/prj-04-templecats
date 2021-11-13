from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

#define the home page of our site
@app.route('/') # sets the route to the current page
def home():
    return render_template("index.html")  # some basic inline html

@app.route('/community_cats')
def community_cats():
    return render_template("ccats.html")

@app.route("/see_cats_outside")
def see_cats_outside():
    return render_template("see_cats_outside.html")

@app.route("/tnr")
def tnr():
    return render_template("tnr.html")

@app.route("/our_kitties")
def our_kitties():
   return render_template("our_kitties.html")

@app.route("/pet_care")
def pet_care():
   return render_tempate("pet_care.html")

@app.route("/donate_volunteer")
def donate_volunteer():
   return render_template("donate_volunteer.html")

#@app.route("/<name>")
#def user(name):
#    print('my name is ', name)
#    return f"Hello {name}!"

# create webpage called admin
@app.route("/admin")
def admin():
    return redirect(url_for('home'))

    # FLASK_APP=tut1.py flask run
