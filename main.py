import random
import time


class Game(object):
    def __init__(self):
        self.places = \
            [['---', '---', '---'],
             ['---', '---', '---'],
             ['---', '---', '---']]
        self.player1 = ''
        self.player2 = ''
        self.counter = 0
        self.if_correct_area = True
        self.play_further = True
        self.its_draw = False
        self.choice_symbol()
        while self.play_further:
            self.pick_place()
            self.bot_player_move()

    def choice_symbol(self):
        while self.player1 != 'X' and self.player1 != 'O':
            self.player1 = input("Choose your player 'X' or 'O': ")
            if self.player1 == 'X':
                self.player2 = 'O'
            elif self.player1 == 'O':
                self.player2 = 'X'

    def pick_place(self):
        self.check_win()
        place_choice = ''
        self.if_correct_area = True
        while self.if_correct_area and self.play_further:
            print(self.places[0])
            print(self.places[1])
            print(self.places[2])
            place_choice = input("Put symbol in place (Row, Column): ").split(' ')
            if self.places[int(place_choice[0])][int(place_choice[1])] != '---':
                print("You can not place symbol in that area!")
                self.if_correct_area = True
            else:
                self.if_correct_area = False
                self.counter += 1
        if self.play_further:
            self.places[int(place_choice[0])][int(place_choice[1])] = self.player1
            print(self.places[0])
            print(self.places[1])
            print(self.places[2])
        else:
            self.counter = 9

    def bot_player_move(self):
        if self.check_win():
            good_choice = True
            if self.counter == 9:
                good_choice = False
                self.play_further = False
            while good_choice:
                column, row = random.randint(0, 2), random.randint(0, 2)
                if self.places[row][column] == '---':
                    print("Bot is picking!")
                    time.sleep(1)
                    self.places[row][column] = self.player2
                    good_choice = False
                    self.counter += 1

    def check_win(self):
        symbols = ['X', 'O']
        for symbol in symbols:
            if (((self.places[0][0] == symbol and self.places[0][1] == symbol and self.places[0][2] == symbol) or
                 (self.places[1][0] == symbol and self.places[1][1] == symbol and self.places[1][2] == symbol) or
                 (self.places[2][0] == symbol and self.places[2][1] == symbol and self.places[2][2] == symbol)) or
                    ((self.places[0][0] == symbol and self.places[1][0] == symbol and self.places[2][0] == symbol) or
                     (self.places[0][1] == symbol and self.places[1][1] == symbol and self.places[2][1] == symbol) or
                     (self.places[0][2] == symbol and self.places[1][2] == symbol and self.places[2][2] == symbol)) or
                    ((self.places[0][0] == symbol and self.places[1][1] == symbol and self.places[2][2] == symbol) or
                     (self.places[0][2] == symbol and self.places[1][1] == symbol and self.places[2][0] == symbol))):
                self.play_further = False
                if self.player1 == symbol:
                    print("Player is winning!")
                elif self.player1 != symbol:
                    print("Bot is winning!")
                print(self.places[0])
                print(self.places[1])
                print(self.places[2])
                return False

        # Jeśli gra nie została przerwana przez wygraną, sprawdzamy czy doszliśmy do remisu
        if self.counter == 9:
            self.play_further = False
            print("It's a draw!")
            print(self.places[0])
            print(self.places[1])
            print(self.places[2])
            return False

        # Jeśli gra nie została przerwana, to kontynuujemy
        return True


tictactoe = Game()
