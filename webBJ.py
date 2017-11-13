from flask import Flask, render_template, request
from black_jack import BlackJack

app = Flask('webBJ')


"""Novo jogo"""
b = BlackJack()
b.shuffle()
pc_hand = b.two_first_cards()
player_hand = b.two_first_cards()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/new_game')
def novo():
    
    handPC = pc_hand
    handPC = b.new_game(pc_hand)
    handPlayer = player_hand
    handPlayer = b.new_game(player_hand)

    jogar()

    return render_template('jogar.html',mJogador = player_hand, pJogador = b.get_point(player_hand), mPC = pc_hand[0])


@app.route('/jogar', methods = ['GET', 'POST'])
def jogar():

    if request.method == 'POST':
        newHand = player_hand
        newHand = b.hit(newHand)

    while (b.get_point(pc_hand) <= 16):
            npc_hand = b.hit(pc_hand)



    return render_template('jogar.html',mJogador = player_hand, pJogador = b.get_point(player_hand), mPC = pc_hand[0])

@app.route('/resultado', methods = ['GET', 'POST'])
def resultado():

        return render_template('resultado.html', resultado = b.bet(b.get_point(pc_hand), b.get_point(player_hand)), mJogador = player_hand, mPC = pc_hand)
