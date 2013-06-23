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
    textos = {
        1: [
            u"Olá bem vindo ao trote game.",
            u"Ou não! hahaha",
            u"Nosso trote é um pouco diferente.",
            u"Você tem a opção de escolher o que você quer fazer.",
            u"Mas se você escolher a opção errada, você vai arcar com as consequências! hahaha"
        ]
    }

    desafios = {
        1: u"Eu sou sua primeira desafiante. Escolha o que você quer fazer enquanto eu tomo uma cerveja:",
    }

    opcoes = {
        1: [
            u"Desafiar na sinuca.",
            u"Desafiar na competição de bebida.",
            u"Tentar fugir para sala 2.",
            u"Tentar fugir para sala 6.",
        ]
    }

    resultados = {
        1: {
            1: {
                "textos": [
                    u"Bem, não foi uma boa ideia ter tomado aquela cerveja antes da sinuca.",
                    u"Se eu não tivesse bebido minha pontaria seria bem melhor.",
                    u"Você não teria me ganhado."
                    u"Agora você pode ir pra sala 2!"
                ],
                "tipo": "passou"
            }
        }
    }

    return render_template("index.html", textos=textos, desafios=desafios, opcoes=opcoes, resultados=resultados)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
