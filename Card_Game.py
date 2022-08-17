'''
Two players are playing a card game. They start with decks of the same size. Each card has a value from 1 to 10. The
game goes as follows:
• On every turn, each player draws a card from the top of their deck and compares the cards that they drew.
• If the value of the first player's card is greater than or equal to the value of the second player's card, the first player takes
both cards and puts them at the bottom of their deck making sure the second player's card is at the bottom.
• If the value of the first player's card is less than the value of the second player's card, the second player takes both cards
and puts them at the bottom of their deck ensuring that the first player's card is at the bottom.
• The game ends when ether player's deck is empty.
You are given two arrays of Integers, deck and deck2. These arrays contain the Initial values of the cards in the first and
the second players' decks. Cards are listed in top-to-bottom order.
Your task is to find how many turns the game will last. Il is guaranteed that the game will end at some point
Example
• For deck = [5] and deck [2] , the output should be solution(deckl, deck2) • 1
Let's consider the game step by step:
• Tum 1:
• The top card from deck is 5 and the top card from deckz is 2
- After drawing top cards from both decks, deck = []and deck2 = []
• Since 5 > 2, 5 and 2 are placed at the bottom of decki
- After the move, decki = [5, 21 ]and deck2 = []
• Since deck2 is empty, the game ends; so the answer is 1
• For deck = [1, 2 ]and deck2 = [3, 1) , the output should be solution(deck1, deck2) = 6
'''
deck1 = [3,2,1,5,6]
deck2 = [1,2,3,6,7]


def cmp(d1, d2, cards1, cards2):
    cards1.pop(0)
    cards2.pop(0)
    if d1>= d2:
        cards1.extend([d1,d2])
    else:
        cards2.extend([d2,d1])
        
# Counting number of iterations until one deck is empty
ctr = 0
       
while deck1 and deck2:
    ctr+=1
    print("Deck1 is -----------------------", deck1)
    print("Deck2 is ------------------------", deck2)
    cmp(deck1[0], deck2[0], deck1, deck2)
print(ctr)
