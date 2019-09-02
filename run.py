import os
from flask import Flask, render_template
import config
import newsconverter as nc
import re

"""
Flask server to run the application: test purposes
"""
dic = {item: getattr(config, item) for item in dir(config) if not item.startswith("__")}

app = Flask(__name__)
@app.route("/")
def home_load():
    dic['BODYCLASS'] = 'homebg'
    # print(dic)
    return render_template('home/index.html', dic=dic)

@app.route("/species")
def species_load():
    dic['BODYCLASS'] = 'speciesbg'
    return render_template('species/index.html', dic=dic)

@app.route("/news")
def news_load():
    dic['BODYCLASS'] = 'newsbg'
    dic['NEWS'] = nc.convert_to_html()
    # print(dic)
    return render_template('news/index.html', dic=dic)

@app.route("/about")
def about_load():
    dic['BODYCLASS'] = 'aboutbg'
    return render_template('about/index.html', dic=dic)

if __name__ == '__main__':
    app.run(debug=True)