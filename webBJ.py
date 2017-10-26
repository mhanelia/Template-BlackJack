from flask import Flask, render_template, request
from black_jack import BlackJack

app = Flask('webBJ')
b = BlackJack()
b.shuffle()
pc_hand = b.two_first_cards()
player_hand = b.two_first_cards()

@app.route('/')
def layout():
    return render_template('layout.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/start')
def start():

    return render_template('jogar.html')

@app.route('/jogar', methods = ['GET', 'POST'])
def jogar():
    if request.method == 'POST':
        newHand = player_hand
        newHand = b.hit(newHand)

    return render_template('jogar.html',mJogador = player_hand, pJogador = b.get_point(player_hand), mPC = pc_hand[0])

@app.route('/resultado', methods = ['GET', 'POST'])
def resultado():
    if request.method == 'GET':

        return render_template('resultado.html', resultado = b.bet(b.get_point(pc_hand), b.get_point(player_hand)))

    return render_template('resultado.html')
