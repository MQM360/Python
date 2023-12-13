# This file runs the Sport Search website.

# Import needed libraries
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request

# Configure application
app = Flask(__name__)
app.secret_key = 'cs50' # Website would not load otherwise? Related to POST?

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Use Cs50's set up to DB to query requests
db = SQL("sqlite:///database_db/sports.db")

# Flask decorator - heps contrrol caching
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Search Function implementation, I used POST because i hope to build on this project over the winter.
@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        searchName = request.form.get("name")

        if not searchName:
            flash("Please Enter a Sport Name")
            return redirect("/")

        # Uses the word entered as a root word to locate a sport
        results = db.execute("SELECT * FROM sports_table WHERE Name LIKE ?",  '%' + searchName + '%')

        if not results:
            flash("Sport Not Found")
            return redirect("/")

        # If results found, forward to results page
        return render_template("results.html", results=results)

    # Handles GET request
    return render_template("search.html")

# Shows the results from the SEARCH functon
@app.route("/results", methods=["POST"])
def results():
    if request.method == "POST":
        searchName = request.form.get("sport")  # Retrieve the sport name from the form

        if not searchName:
            flash("Please Enter a Sport Name")
            return redirect("/")  # Redirect to the home page if the input is empty

        # Perform a database query based on the search_name
        results = db.execute("SELECT Name, Location FROM sports_table WHERE Name LIKE ?", '%' + searchName + '%')

        if not results:
            flash("Sport Not Found")
            return redirect("/")

        return render_template("results.html", results=results)
    # print(results) # Debug
    # Handle GET requests or other cases by redirecting to the home page
    return redirect("/")

# Used to go back to search page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("search.html")
