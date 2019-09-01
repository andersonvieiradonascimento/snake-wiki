import os
from flask import Flask, render_template
import config

"""
Flask server to run the application: test purposes
"""
dic = {item: getattr(config, item) for item in dir(config) if not item.startswith("__")}

app = Flask(__name__)
@app.route("/")
def home_load():
    return render_template('home/index.html', dic=dic)

@app.route("/species")
def species_load():
    return render_template('species/index.html', dic=dic)

@app.route("/news")
def news_load():
    return render_template('news/index.html', dic=dic)

@app.route("/about")
def about_load():
    return render_template('about/index.html', dic=dic)

if __name__ == '__main__':
    app.run(debug=True)