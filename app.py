from flask import Flask, send_from_directory
from flask import request as f_request 
import logging

import os

import sys,requests,json, pprint, datetime

app = Flask(__name__, static_url_path = '',static_folder = 'static')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def get_article_list():
    #list all folders in root content directory - 
    # they contain articles from specific category.
    article_categories = [
        c for c in os.listdir('content') 
        if os.path.isdir(os.path.join('content',c))
        ]
    
    #in every category enter all of the subfoders,
    #to collect all meta.json files - they contain
    #metadata needed to render specific article.
    meta_jsons = []
    for c in article_categories:
        meta_jsons.extend(
            [
                os.path.join('content',c,a,'meta.json')
                for a in os.listdir(os.path.join('content',c))
            ]
        )
    #attempt to load json from every found .json file,
    #and put them in a single list.
    article_list = []
    for j in meta_jsons:
        try:
            with open(j,'r') as fh:
                loaded_json = json.load(fh)
                article_list.append(loaded_json)
        except JSONDecodeError as e:
            logging.warning("invalid JSON found in file "+ str(j))
        except (OSError, IOError) as e:
            logging.warning("error opening json file "+ str(j)+" - reason: " + str(e))
    print("loaded JSON:")
    print(json.dumps(article_list,indent=2))
    return article_list
    

article_tree_list = get_article_list() 

@app.route("/<path:path>")
def serve_spa(path):
    return send_from_directory('',path)

@app.route("/api/list")
def get_list():
    return json.dumps(article_tree_list)

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

@app.route("/api/article")
def get_article_by_tag():
    tag = f_request.args.get('tag')
    if type(tag) is not str:
        return get_md_404()
    matching_articles = [aj for aj in article_tree_list if aj['tag'] == tag]
    if len(matching_articles) == 1:
        return get_md_by_meta(matching_articles[0])
    if len(matching_articles) == 0:
        return get_md_404()
    else:
        logging.warning("multiple articles with same tag found - this is bad.")
        return get_md_by_meta(matching_articles[0])
    
def elo():
    pass

