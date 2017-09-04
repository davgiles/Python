#  File: War.py
#  Description: A simulation of the 2-player card game, War!
#  Student's Name: David Giles
#  Student's UT EID: dgg524
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 06/15/17
#  Date Last Modified: 06/22/17

import random

class Card:

    suits = ['C', 'D', 'H', 'S']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return(self.rank+self.suit)

class Deck:

    def __init__(self):
        cardList = []

        for i in range(len(Card.suits)):
            for j in range(len(Card.ranks)):
                cardList.append(str(Card(Card.ranks[j],Card.suits[i])))

        self.cardList = cardList

    def __str__(self):
        idx = 0
        deck = ''
        for i in range(len(self.cardList)):
            if i != 0 and i % 13 == 0:
                deck += '\n'
            deck += '{:>4}'.format(self.cardList[i])
        return(deck)

    # shuffles the deck of cards into a random order
    def shuffle(self):
        random.shuffle(self.cardList)

    # deals one card from the deck to a player
    def dealOne(self, player):
        player.hand.append(self.cardList.pop(0))
        player.handTotal += 1

class Player:

    player_count = 0 # simple counter for number of players in game
    def __init__(self):
        self.hand = []
        self.handTotal = 0
        Player.player_count += 1
        self.id = Player.player_count

    def __str__(self):
        idx = 0
        hand = ''
        for i in range(len(self.hand)):
            if i != 0 and i % 13 == 0:
                hand += '\n'
            hand += '{:>4}'.format(self.hand[i])
        return(hand)

    # checks if player has any cards in hand
    def handNotEmpty(self):
        if self.handTotal > 0:
            return True
        else:
            return False


def playGame(deck, player1, player2):
    print('\n\nInitial hands:\nPlayer 1:')
    print(player1)
    print('\n\nPlayer 2:')
    print(player2)

    round = 1
    gameOver = False
    while not gameOver:
        pile1 = []  # list for cards played by player1
        pile2 = []  # list for cards played by player2
        war = False

        print('\n\nROUND '+str(round)+':')

        print('Player 1 plays:{:>4}'.format(str(player1.hand[0])))
        playCard(player1, pile1)
        print('Player 2 plays:{:>4}'.format(str(player2.hand[0])))
        playCard(player2, pile2)
        print()

        # if the last card played by each player are equal in value, war begins
        if faceVal(pile1[-1]) == faceVal(pile2[-1]):
            war = True
            print('War starts:{:>4} ={:>4}'.format(pile1[-1], pile2[-1]))
        # if player 1's card is greater in value than player 2's card, player 1 wins
        elif faceVal(pile1[-1]) > faceVal(pile2[-1]):
            print('\nPlayer 1 wins round {}:{:>4} >{:>4}\n'.format(str(round), pile1[-1], pile2[-1]))
            collectCards(player1, pile1, pile2)
        # if player 2's card is greater in value than player 1's card, player 2 wins
        elif faceVal(pile1[-1]) < faceVal(pile2[-1]):
            print('\nPlayer 2 wins round {}:{:>4} >{:>4}\n'.format(str(round), pile2[-1], pile1[-1]))
            collectCards(player2, pile1, pile2)
        else:
            pass

        # in the case of war, run this loop until a player wins the round
        while war:
            for i in range(3):
                print('Player 1 puts{:>4} face down'.format(player1.hand[0]))
                playCard(player1, pile1)
                print('Player 2 puts{:>4} face down'.format(player2.hand[0]))
                playCard(player2, pile2)
            print('Player 1 puts{:>4} face up'.format(player1.hand[0]))
            playCard(player1, pile1)
            print('Player 2 puts{:>4} face up'.format(player2.hand[0]))
            playCard(player2, pile2)

            if faceVal(pile1[-1]) > faceVal(pile2[-1]):
                print('\nPlayer 1 wins round {}:{:>4} >{:>4}\n'.format(str(round), pile1[-1], pile2[-1]))
                collectCards(player1, pile1, pile2)
                war = False
            elif faceVal(pile1[-1]) < faceVal(pile2[-1]):
                print('\nPlayer 2 wins round {}:{:>4} >{:>4}\n'.format(str(round), pile2[-1], pile1[-1]))
                collectCards(player2, pile1, pile2)
                war = False
            else:
                print('\nWar continues: {:>4} ={:>4}')

        print('Player 1 now has', player1.handTotal, 'card(s) in hand:')
        print(player1)
        print('Player 2 now has', player2.handTotal, 'card(s) in hand:')
        print(player2)

        if player1.handTotal == 0 or player2.handTotal == 0:
            gameOver = True

        round += 1

# this function takes the top card from the players hand and plays it onto the table
def playCard(player, pile):
    pile.append(player.hand.pop(0))
    player.handTotal -= 1
    
# this function puts the cards that were played for the round into the winner's hand
def collectCards(player, pile1, pile2):
    for card in pile1:
        player.hand.append(card)
        player.handTotal += 1
    for card in pile2:
        player.hand.append(card)
        player.handTotal += 1

# converts face value of card to int
def faceVal(card):
    if card[:-1] == 'J':
        return 11
    elif card[:-1] == 'Q':
        return 12
    elif card[:-1] == 'K':
        return 13
    elif card[:-1] == 'A':
        return 14
    else:
        return int(card[:-1])


def main():
    cardDeck = Deck()  # create a deck of 52 cards called "cardDeck"

    print("Initial deck:")
    print(cardDeck)  # print the deck so we can see that you built it correctly

    random.seed(15)  # leave this in for grading purposes
    cardDeck.shuffle()  # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)  # print the deck so we can see that your shuffle worked

    player1 = Player()  # create a player
    player2 = Player()  # create another player

    for i in range(26):  # deal 26 cards to each player, one at
        cardDeck.dealOne(player1)  # a time, alternating between players
        cardDeck.dealOne(player2)

    playGame(cardDeck, player1, player2)

    if player1.handNotEmpty():
        print("\n\nGame over.  Player 1 wins!")
    else:
        print("\n\nGame over.  Player 2 wins!")

    print("\n\nFinal hands:")
    print("Player 1:   ")
    print(player1)  # printing a player object should print that player's hand
    print("\nPlayer 2:")
    print(player2)  # one of these players will have all of the cards, the other none


main()
