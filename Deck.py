from Card import Card

class Deck:

    def __init__(self):

        self.cards = self.MakeDeck()

    def MakeDeck(self):

        cards = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        for suit in suits:

            cardNumber = 1
            while cardNumber < 14:
                
                cardNumberRepresentation = str(cardNumber)
                if cardNumber == 1:
                    cardNumberRepresentation = "A"
                elif cardNumber == 11:
                    cardNumberRepresentation = "J"
                elif cardNumber == 12:
                    cardNumberRepresentation = "Q"
                elif cardNumber == 13:
                    cardNumberRepresentation = "K"
                
                cards.append(Card(cardNumberRepresentation, cardNumber, suit))
                cardNumber += 1
        
        return cards
    
    def ShowCards(self):

        for card in self.cards:
            print(card.number + " of " + card.suit)
