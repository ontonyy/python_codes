from random import shuffle

class Card:
    suits = ['picks', 'worms', 'bubies', 'crosses']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'knave', 'lady', 'king', 'ace']
    
    def __init__(self, v, s):
        self.value = v
        self.suit = s
    
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        v = self.values[self.value] + " " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input('Name player 1: ')
        name2 = input('Name player 2: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = f"{winner} takes away cards"
        print(w)
    
    def draw(self, p1n, p2n, p1c, p2c):
        d = f"\n{p1n} puts {p1c}, but {p2n} puts {p2c}"
        print(d)
    
    def play_game(self):
        cards = self.deck.cards
        print("Let's GO!")
        while len(cards) >= 2:
            response = input("\nPress 'X' for exit. Press another one key for continue gaming.")
            if response == 'X':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p2n, p1c, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)            
            else:
                self.p2.wins += 2
                self.wins(self.p2.name)
        
        win = self.winner(self.p1, self.p2)

        print(f"Game over. {win} won!")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p1.wins < p2.wins:
            return p2.name
        else:
            return "Tie!"
        
game = Game()
game.play_game()
