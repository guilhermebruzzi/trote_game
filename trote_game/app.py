#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from flask import Flask, redirect, url_for, session, request, abort, make_response
from config import get_app, project_root
from helpers import render_template


app = get_app() #  Explicitando uma variável app nesse arquivo para o Heroku achar

def __make_response_plain_text__(response_text):
    response = make_response(response_text)
    response.headers["Content-type"] = "text/plain"
    return response

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    return __make_response_plain_text__(open('%s/trote_game/static/sitemap.xml' % project_root).read())


@app.route('/robots.txt', methods=['GET'])
def robots():
    return __make_response_plain_text__(open('%s/trote_game/static/robots.txt' % project_root).read())

@app.route('/', methods=['GET', 'POST'])
def index():
    textos = [
        u"Olá bem vindo ao trote game",
        u"Ou não! hahaha"
    ]
    textos1 = textos2 = textos3 = textos4 = textos5 = textos6 = textos
    return render_template("index.html",
        textos1=textos1, textos2=textos2,textos3=textos3,textos4=textos4,textos5=textos5,textos6=textos6)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
