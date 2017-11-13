"""Lógica do BlackJack."""
import random
from os import system as system_call



class BlackJack(object):
    """Classe que implementa a Lógica do BlackJack."""

    def __init__(self):
        """Método construtor da classe."""
        self.numbers = ["A", "2", "3", "4", "5", "6", "7",
                        "8", "9", "10", "Q", "J", "K"]

        self.suits = ["♣", "♦", "♥", "♠"]

        self.deck = self.create_deck()

    def create_deck(self):
      deck = []
      for i in self.numbers:
          for x in self.suits:
              deck.append(i+x)
      return deck

    def new_game(self, mao):
        self.deck = []
        mao = []
        random.shuffle(self.deck)
        return mao

    def shuffle(self):
        random.shuffle(self.deck)

    def two_first_cards(self):
        cards = []
        cards.append(self.deck[:2])
        del self.deck[:2]
        system_call("cls")
        return cards

    def hit(self, mao):

        mao.append(self.deck[:1])
        del self.deck[:1]

        return mao


    def get_point(self, mao):
        point = 0
        for item in mao:
            for card in item:
                card = card.replace("♣","").replace("♦","").replace("♥","").replace("♠","")
                if (card == "Q" or card == "J" or card == "K" ):
                    point = point + 10

                elif (card == "A"):
                    point = point + 1

                else:
                    point = point + int(card)

        return point


    def show_hand(self, name, cards, point):
         return "Jogador: {} - Cartas {}\n Pontos {}".format(name,cards,point)


    def bet(self,pc, player):

        if (player == pc):
            return "Empate!".format(pc)

        elif ((pc > player) and (pc <= 21)):
            return "Vencedor: Maquina Pontos: {}\n Perdedor: Murilo Pontos: {}".format(pc, player)

        elif (player > pc) and (player <= 21):
            return "Vencedor: Murilo Pontos: {} \n Perdedor: Maquina Pontos: {}".format(player,pc)

        elif (pc > player) and (pc > 21):
            return "Vencedor: Murilo Pontos: {}\n Perdedor: Maquina Pontos: {}".format(player,pc)

        elif (player > pc) and (player > 21):
            return "Vencedor: Maquina Pontos: {} \n Perdedor: Murilo Pontos: {}".format(pc, player)
