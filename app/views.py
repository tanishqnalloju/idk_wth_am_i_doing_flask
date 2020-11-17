from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/merge_sort")
def merge_sort():
    return render_template("public/sort.html", Name = "Merge", Job = "Sort", Description ="Merge Sort fasteets sort")

@app.route("/bubble_sort")
def bubble_sort():
    return render_template("public/sort.html", Name = "Bubble", Job = "Sort")

@app.route("/linear_search")
def linear_sort():
    return render_template("public/sort.html", Name = "Linear", Job = "Search")

@app.route("/binary_search")
def binary_sort():
    return render_template("public/sort.html", Name = "Binary", Job = "Search")
