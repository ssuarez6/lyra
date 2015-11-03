# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-

from flask import render_template
from app import app

@app.route("/main")
@app.route('/index')
@app.route('/')
def hello():
    return render_template("index.html")