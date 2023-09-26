import random
import time
from hand_strength import HandStrength
from operator import itemgetter

#Game variables:
starting_chips = 5000
bb = 100
sb = bb/2
max_players = 7

class Player:
    min_bet = bb
    cur_bet = 0
    total_hand_bet = 0
    isBtn = False
    inTheHand = True
    inTheGame = True

    def __init__(self, seat, cards=[]):
        self.chips = random.randint(4000, 5000)
        self.seat = seat
        self.cards = cards
    
    def PrintCards(self):
        print(f"[{self.cards[0]} {self.cards[1]} {self.cards[2]} {self.cards[3]} {self.cards[4]}]")

    def AllIn(self):
        pass
    
    def Bet(self, bet):
        pass


def Hand(table):
    pot = [0] * max_players
    print(pot) 
    deck = ["2A", "3A", "4A", "5A", "6A", "7A", "8A", "9A", "TA", "JA", "QA", "KA", "AA",
    "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "TB", "JB", "QB", "KB", "AB",
    "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC", "JC", "QC", "KC", "AC",
    "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD", "JD", "QD", "KD", "AD"]

    def SetPots():
        #Count Chips
        chips_arr = []
        for i in range(0, len(table)):
            chips_arr.append([table[i].chips, i])
        chips_arr.sort()
        pot_max = []
        pot_idx = []
        prev = 0
        for i in range(0, len(chips_arr)):
            pot_max.append(chips_arr[i][0]-prev)
            prev = chips_arr[i][0]
            pot_idx.append(chips_arr[i][1])
        print(chips_arr, pot_max, pot_idx)

    def nextPlayer(cur):
        #Finds the next player to the left of i  (0~6)
        for i in range(0,  len(table)):
            if i>cur:
                if table[i].inTheGame == True:
                    return i
        for i in range(0, len(table)):
            if table[i].inTheGame == True:
                return i
        
    def RotateBtn():
        btn = 999
        for i in range(0, len(table)):
            if table[i].isBtn == True:
                table[i].isBtn = False
                btn = i
            if i>btn:
                if table[i].inTheGame == True:
                    table[i].isBtn = True
                    return i
        for i in range(0, len(table)):
            if table[i].inTheGame == True:
                table[i].isBtn = True
                return i
        return -1

    def Deal():
        for p in table:
            if p.inTheGame:
                p.inTheHand = True
                #First card
                card = random.choice(deck)
                deck.remove(card)
                p.cards.append(card)
                #Second card
                card = random.choice(deck)
                deck.remove(card)
                p.cards.append(card)
                #Third card
                card = random.choice(deck)
                deck.remove(card)
                p.cards.append(card)
                #Fourth card
                card = random.choice(deck)
                deck.remove(card)
                p.cards.append(card)
                #Fifth card
                card = random.choice(deck)
                deck.remove(card)
                p.cards.append(card)
                p.PrintCards()
        return

    def Blinds(sb_pos, bb_pos):
        if table[sb_pos].chips <= sb:
            table[sb_pos].AllIn()
        else:
            table[sb_pos].Bet(sb)

        if table[bb_pos].chips <= bb:
            table[bb_pos].AllIn()
        else:
            table[bb_pos].Bet(bb) 

    def Betting():
        pass

    SetPots() 
    btn_pos = RotateBtn()
    Blinds(nextPlayer(btn_pos), nextPlayer(nextPlayer(btn_pos)))
    Deal()
    Betting()
    return

def Game():
    table = []
    for i in range(0, max_players): table.append(Player(i, [])) #We must pass "[]" otherwise all of the cards will be linked
    table[0].isBtn = True
    while(1):            
        Hand(table)
        left = 0
        for i in range(0, len(table)):
            if table[i].chips <= 0:
                table[i].inTheGame = False

            if table[i].inTheGame:
                left+=1
                index = i
        if left == 1:
            print(f"Player {index} won")
            return

        print("Next hand starting soon")
        time.sleep(3)
Game()