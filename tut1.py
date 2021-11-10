from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

#define the home page of our site
@app.route('/') # sets the route to the current page
def home():
    return render_template("index.html", dexter={"dog":7, "smell":"bad"})  # some basic inline html

@app.route("/<name>")
def user(name):
    print('my name is ', name)
    return f"Hello {name}!"

# create webpage called admin
@app.route("/admin")
def admin():
    return redirect(url_for('home'))