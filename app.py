from flask import Flask, send_from_directory
from flask import request as f_request 
import logging

from json import JSONDecodeError

import os

import sys,requests,json, pprint, datetime

app = Flask(__name__, static_url_path = '',static_folder = 'static')


#for my local testing
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def get_article_tree():
    #list all folders in root content directory - 
    # they contain articles from specific category.

    article_categories = [
        {'name':c,'articles':[]} for c in os.listdir('content') 
        if os.path.isdir(os.path.join('content',c))
        ]

    
    #in every category enter all of the subfoders,
    #to collect all meta.json files - they contain
    #metadata needed to render specific article.
    for category in article_categories:
        category['articles'].extend(
            [
                load_meta_by_filepath(
                    os.path.join('content',category['name'],arts,'meta.json')
                    )
                for arts in os.listdir(os.path.join('content',category['name']))
            ]
        )
    
    print("loaded JSON:")
    print(json.dumps(article_categories,indent=2))
    return article_categories

def load_meta_by_filepath(filepath):
    # Attenpt opening JSON by its filepath
    try:
        with open(filepath,'r') as fh:
            loaded_json = json.load(fh)
            return(loaded_json)
    except JSONDecodeError as e:
        logging.warning("invalid JSON found in file "+ str(j))
        return {}
    except (OSError, IOError) as e:
        logging.warning("error opening json file "+ str(j)+" - reason: " + str(e))
        return {}


article_tree = get_article_tree() 

@app.route("/<path:path>")
def serve_spa(path):
    return send_from_directory('',path)

@app.route("/")
def serve_index():
    return send_from_directory('','index.html')

@app.route("/api/list")
def get_list():
    return json.dumps(article_tree)


def get_md_by_meta(meta_dict):
    path_by_meta = \
        os.path.join(
            'content',
            meta_dict['category'],
            meta_dict['tag'],
            'content.md'
        ).replace('..',"i-may-be-paranoid")
    
    with open(path_by_meta,'r') as fh:
        return fh.read()

def get_md_404(reason = "rekt"):
    return "rekt. Because "+ str(reason)

@app.route("/api/article/<string:category>/<string:article_tag>")
def get_article_by_path(category,article_tag):
    try:
        articles_from_category = [
            afc for afc in article_tree
            if afc['name'] == category][0]['articles']
        
        article_meta = [
            a for a in articles_from_category
            if a['tag'] == article_tag
        ][0]
        print(json.dumps(article_meta,indent=2))
        return get_md_by_meta(article_meta)
    except:
        return get_md_404()
