import stories.py

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/form.html")
def some_form():
    return render_template("form.html")

@app.route("/story.html")
def generate_story():
    return render_template("story.html") 


story.generate()