from flask import Flask
from flask import request as f_request 

import sys,requests,json, pprint, datetime

app = Flask(__name__)

@app.route("/")
def serve_spa():
    return ""

@app.route("/api/list")
def get_article_list():
    return ""

@app.route("/api/article")
def get_article_by_name():
    return ""

def elo():
    pass