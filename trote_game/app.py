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
        ],
        2: [
            u"Bom dia, calouro!",
            u"Vemos que você conseguiu vencer o primeiro desafio.",
            u"E isso me deixa muito irritado.",
            u"É bom você tomar cuidado...",
        ],
        3: [
            u"Hmm, num é muito comum os calouros chegarem nessa sala.",
            u"É bom que você não esteja trapaceando.",
            u"Você não imagina o que a gente faz com quem trapaceia...",
            u"Mas tudo bem... Da mesma forma que quase nenhum calouro chega aqui, quase nenhum sai daqui vitorioso.",
            u"Vamos ao que interessa...",
        ],
        4: [
            u"Olha o que temos aqui... Um calouro.",
            u"Como você chegou nessa sala?",
            u"Se eu descobrir que você anda trapaceando por aí, você vai se ver comigo...",
        ],
        7: [
            u"Parabéns, você está bem perto...",
        ]
    }

    desafios = {
        1: u"Eu sou sua primeira desafiante. Escolha o que você quer fazer enquanto eu tomo uma cerveja:",
        2: u"Não me faça perder mais tempo, escolhe logo o que você quer!:",
        3: u"O que você deseja fazer?",
        4: u"O que você deseja fazer agora?",
    }

    opcoes = {
        1: [
            u"Desafiar na sinuca.",
            u"Desafiar na competição de bebida.",
            u"Tentar fugir para sala 2.",
            u"Tentar fugir para sala 3.",
        ],
        2: [
            u"Desafiar na queda de braço.",
            u"Desafiar na amarelinha.",
            u"Tentar fugir para sala 3.",
            u"Tentar fugir para sala 5.",
        ],
        3: [
            u"Desafiar na competição de bebida.",
            u"Desafiar na bola de gude.",
            u"Tentar fugir para sala 5.",
            u"Tentar fugir para sala 6.",
        ],
        4: [
            u"Desafiar na amarelinha.",
            u"Desafiar no totó.",
            u"Tentar fugir para sala 6.",
            u"Tentar fugir para a super sala.",
        ],
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
                "tipo": "passou",
                "sala": 2
            },
            2: {
                "textos": [
                    u"Você já bebeu alguma vez na vida?",
                    u"Foi muito fácil ganhar de você! hahaha"
                ],
                "tipo": "perdeu"
            },
            3: {
                "textos": [
                    u"Hmm, espertinho você.",
                    u"Você achou mesmo que eu não ia perceber que você tentou fugir?"
                ],
                "tipo": "perdeu"
            },
            4: {
                "textos": [
                    u"Ora, cadê o calouro?",
                    u"Alguém levou ele pra outra sala?",
                ],
                "tipo": "passou",
                "sala": 3
            }
        },
        2: {
            1: {
                "textos": [
                    u"Você achou mesmo que me ganharia na queda de braço?",
                    u"Na queda de braço?",
                    u"Você não tem força nem pra levantar uma pena!"
                ],
                "tipo": "perdeu",
            },
            2: {
                "textos": [
                    u"Amarelinha é um jogo de criança.",
                    u"Não me surpreende que você tenha ganhado.",
                    u"Vai logo pra sala 3.",
                ],
                "tipo": "passou",
                "sala": 3
            },
            3: {
                "textos": [
                    u"Hmm, espertinho você.",
                    u"Você achou mesmo que eu não ia perceber que você tentou fugir?"
                ],
                "tipo": "perdeu"
            },
            4: {
                "textos": [
                    u"Ora, cadê o calouro?",
                    u"Alguém levou ele pra outra sala?",
                ],
                "tipo": "passou",
                "sala": 5
            }
        },
        3: {
            1: {
                "textos": [
                    u"Você já bebeu alguma vez na vida?",
                    u"Foi muito fácil ganhar de você! hahaha"
                ],
                "tipo": "perdeu",
            },
            2: {
                "textos": [
                    u"Amarelinha é um jogo de criança.",
                    u"Não me surpreende que você tenha ganhado.",
                    u"Vai logo pra sala 3.",
                ],
                "tipo": "passou",
                "sala": 4
            },
            3: {
                "textos": [
                    u"Ora, cadê o calouro?",
                    u"Alguém levou ele pra outra sala?",
                ],
                "tipo": "passou",
                "sala": 5
            },
            4: {
                "textos": [
                    u"Ora, cadê o calouro?",
                    u"Alguém levou ele pra outra sala?",
                ],
                "tipo": "passou",
                "sala": 6
            }
        },
        4: {
            1: {
                "textos": [
                    u"Amarelinha é um jogo de criança.",
                    u"Não me surpreende que você tenha ganhado.",
                    u"Vai logo pra sala 3.",
                ],
                "tipo": "passou",
                "sala": 5
            },
            2: {
                "textos": [
                    u"",
                    u"Não me surpreende que você tenha ganhado.",
                    u"Vai logo pra sala 3.",
                ],
                "tipo": "passou",
                "sala": 6
            },
            3: {
                "textos": [
                    u"Hmm, espertinho você.",
                    u"Você achou mesmo que eu não ia perceber que você tentou fugir?"
                ],
                "tipo": "perdeu",
            },
            4: {
                "textos": [
                    u"Hmm, espertinho você.",
                    u"Você achou mesmo que eu não ia perceber que você tentou fugir?"
                ],
                "tipo": "perdeu",
            }
        },
    }

    return render_template("index.html", textos=textos, desafios=desafios, opcoes=opcoes, resultados=resultados)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
