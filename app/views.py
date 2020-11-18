from app import app

from flask import render_template, request, flash, url_for

#Importing pre defined Sorting and Searching models
#from CustomModels import MergeSort as ms, BubbleSort as bus, BinarySearch as bis, LinearSearch as ls
from app.CustomModels import ms, ls, bus, bis
from app.Sort import bubbleSort as bsort, mergeSort as msort 
from app.Search import linear_search as lsearch, binary_search as bsearch

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/merge_sort", methods = ['GET', 'POST'])
def merge_sort():
    if request.method == 'POST':
        # flash("LOL")
        input_text = request.form['input']
        print(msort(input_text))
        render_template("public/sort.html", message = "LOL")
    return render_template("public/sort.html", Name = ms.Name, Job = ms.Job, Description = ms.Description, tc_img = ms.TComp, sc_img = ms.SComp, message = None)

@app.route("/bubble_sort", methods = ['GET', 'POST'])
def bubble_sort():
    if request.method == 'POST':
        # flash("LOL")
        input_text = request.form['input']
        message = msort(input_text)

        render_template("public/sort.html", message = "LOL")
    return render_template("public/sort.html", Name = bus.Name, Job = bus.Job, Description = bus.Description, tc_img = bus.TComp, sc_img = bus.SComp)

@app.route("/linear_search", methods = ['GET', 'POST'])
def linear_search():
    if request.method == 'POST':
        input_text = request.form['input']
        key = request.form['search_ele']
        message = lsearch(input_text, key)
        print(message)
        render_template("public/sort.html", message = "message")
    return render_template("public/sort.html", Name = bis.Name, Job = bis.Job, Description = bis.Description, tc_img = bis.TComp, sc_img = bis.SComp)

@app.route("/binary_search", methods = ['GET', 'POST'])
def binary_search():
    if request.method == 'POST':
        input_text = request.form['input']
        key = request.form['search_ele']
        message = bsearch(input_text, key)
        print(message, request.form['file_up'])
        render_template("public/sort.html", message = message)

    return render_template("public/sort.html", Name = ls.Name, Job = ls.Job, Description = ls.Description, tc_img = ls.TComp, sc_img = ls.SComp)
