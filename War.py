from Deck import Deck
from AI import AI
import random

def log(log):
    logFile = open("/home/vincent/Development/Fun/War/War_Log.log","a")
    logFile.write(log + "\n")
    logFile.close()
    print(log)

def CreateArsenals(deck, player1, player2):

    if len(deck.cards) != 52:
        log("Deck of cards does not have 52 cards, fix that.")
        exit()
    
    player1.arsenal = []
    player2.arsenal = []

    for index, card in enumerate(deck.cards):
        
        if index % 2 == 0:
            player1.arsenal.append(deck.cards[index])
        else:
            player2.arsenal.append(deck.cards[index])
    
    if len(player1.arsenal) == 26 and len(player2.arsenal) == 26:
        deck.cards = []

def Play(player1, player2):

    while player1.won == False and player2.won == False:

        player1CardBeingPlayed = player1.PlayTopCard()
        log(player1.name + " played " + player1CardBeingPlayed.number + " of " + player1CardBeingPlayed.suit)
        player2CardBeingPlayed = player2.PlayTopCard()
        log(player2.name + " played " + player2CardBeingPlayed.number + " of " + player2CardBeingPlayed.suit)

        if player1CardBeingPlayed.realNumber == player2CardBeingPlayed.realNumber:
            GoToWar(player1CardBeingPlayed.number, [player1CardBeingPlayed, player2CardBeingPlayed], player1, player2)
        elif player1CardBeingPlayed.realNumber > player2CardBeingPlayed.realNumber:
            log(player1.name + " won the hand. They take both cards.")
            player1.AddCardToArsenal(player1CardBeingPlayed)
            player1.AddCardToArsenal(player2CardBeingPlayed)
            log(player1.name + " has " + str(len(player1.arsenal)) + " cards in their arsenal.")
        elif player1CardBeingPlayed.realNumber < player2CardBeingPlayed.realNumber:
            log(player2.name + " won the hand. They take both cards.")
            player2.AddCardToArsenal(player1CardBeingPlayed)
            player2.AddCardToArsenal(player2CardBeingPlayed)
            log(player2.name + " has " + str(len(player2.arsenal)) + " cards in their arsenal.")
        
        if (len(player1.arsenal) == 0):
            player2.won = True
        elif (len(player2.arsenal) == 0):
            player1.won = True
    
    if (player1.won):
        log(player1.name + " won!")
    else:
        log(player2.name + " won!")
    
    log(player1.name + " played " + str(player1.moves) + " moves.")
    log(player2.name + " played " + str(player2.moves) + " moves.")

def GoToWar(numberInQuestion, gamePile, player1, player2):

    player1CurrentWarCard = ""
    player2CurrentWarCard = ""

    while True:

        player1CurrentWarCard = player1.PlayTopCard()
        player2CurrentWarCard = player2.PlayTopCard()

        if (player1CurrentWarCard == None or player2CurrentWarCard == None):
            return

        gamePile.append(player1CurrentWarCard)
        gamePile.append(player2CurrentWarCard)
    
        if player1CurrentWarCard.number == numberInQuestion:
            player1.arsenal += gamePile
            log(player1.name + " won the war. They take " + str(len(gamePile)) + " cards.")
            log(player1.name + " has " + str(len(player1.arsenal)) + " cards in their arsenal.")
            break
        elif player2CurrentWarCard.number == numberInQuestion:
            player2.arsenal += gamePile
            log(player2.name + " won the war. They take " + str(len(gamePile)) + " cards.")
            log(player2.name + " has " + str(len(player2.arsenal)) + " cards in their arsenal.")
            break

totalWinsAI1 = 0
totalWinsAI2 = 0

#Empty log
with open("/home/vincent/Development/Fun/War/War_Log.log","r+") as logFile:
    logFile.truncate()

#Create AIs
AI1 = AI("Vince")
AI2 = AI("Jason")

while True:
    #Prove deck of cards was built properly
    deck = Deck()
    log("Created deck of cards...")

    #Shuffle deck of cards
    random.shuffle(deck.cards)
    log("Shuffled deck of cards...")

    #Give players their arsenals
    CreateArsenals(deck, AI1, AI2)
    #Check count of cards to make sure all is good
    log(AI1.name + " has " + str(len(AI1.arsenal)) + " in their arsenal.")
    #AI1.ShowArsenal()
    log(AI2.name + " has " + str(len(AI2.arsenal)) + " in their arsenal.")
    #AI2.ShowArsenal()
    log("Main deck has " + str(len(deck.cards)) + " cards left.")


    log("Let's play!")
    Play(AI1, AI2)

    if AI1.won:
        totalWinsAI1 += 1
        AI1.won = False
    elif AI2.won:
        totalWinsAI2 += 1
        AI2.won = False
    
    print(AI1.name + " total wins: " + str(totalWinsAI1) + " | " + AI2.name + " total wins: " + str(totalWinsAI2))


