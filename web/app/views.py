# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-

from flask import render_template, redirect, url_for, request, json
from app import app

@app.route("/main")
@app.route('/index')
@app.route('/')
def hello():
    return render_template("test.html")