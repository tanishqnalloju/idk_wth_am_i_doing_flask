from flask import Flask, render_template, request, flash, url_for

app = Flask(__name__)

#Importing data models to represent the Name, Jobs nd other fields in sort.html
from CustomModels import ms, ls, bus, bis
#Importing pre defined Sorting and Searching models
#from CustomModels import MergeSort as ms, BubbleSort as bus, BinarySearch as bis, LinearSearch as ls
from Sort import bubbleSort as bsort, mergeSort as msort
from Search import linear_search as lsearch, binary_search as bsearch

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/merge_sort", methods = ['GET', 'POST'])
def merge_sort():
    if request.method == 'POST':
        input_text = request.form['input']
        print(input_text)
        message = msort(input_text)
        return render_template("public/sort.html", ren_list = input_text, message = message, Cust_Model = ms)
    return render_template("public/sort.html", Cust_Model = ms)

@app.route("/bubble_sort", methods = ['GET', 'POST'])
def bubble_sort():
    if request.method == 'POST':
        input_text = request.form['input']
        message = bsort(input_text)
        return render_template("public/sort.html", ren_list = input_text, message = message, Cust_Model = bus)
    return render_template("public/sort.html", Cust_Model = bus)

@app.route("/linear_search", methods = ['GET', 'POST'])
def linear_search():
    if request.method == 'POST':
        input_text = request.form['input']
        key = request.form['search_ele']
        message, index = lsearch(input_text, key)
        return render_template("public/sort.html", ren_list = input_text, ren_ele = key, message = message, Cust_Model = ls, index = index )
    return render_template("public/sort.html", Cust_Model = ls)

@app.route("/binary_search", methods = ['GET', 'POST'])
def binary_search():
    if request.method == 'POST':
        input_text = request.form['input']
        key = request.form['search_ele']
        message, index = bsearch(input_text, key)
        return render_template("public/sort.html", ren_list = input_text, ren_ele = key, message = message, Cust_Model = ms, index = index)
    return render_template("public/sort.html", Cust_Model = bis)

if __name__ == "__main__":
    app.run(debug = True)
