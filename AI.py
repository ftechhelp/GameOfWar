class AI:

    def __init__(self, name):

        self.name = name
        self.arsenal = []
        self.won = False
        self.moves = 0
    
    def AddCardToArsenal(self, card):
        self.arsenal.append(card)
    
    def PlayTopCard(self):

        self.moves += 1
        if len(self.arsenal) == 0:
            return None

        card = self.arsenal[0]
        del self.arsenal[0]

        return card
    
    def ShowArsenal(self):

        for card in self.arsenal:
            print(card.number + " of " + card.suit)
