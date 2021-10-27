hearts = ["A-H", "K-H", "Q-H", "J-H", "10-H", "9-H", "8-H", "7-H", "6-H", "5-H", "4-H", "3-H", "2-H"]
stack = hearts

import random

print("Let's play Hearts. Here are the cards: ",', '.join(hearts))
prompt = ":> "
your_hand = []

for i in range(0,3):
    dealt_card_index = random.randint(0,len(stack)-1)

    #dealt_card = hearts.remove(random.choice(hearts))
    #print(dealt_card_index)
    dealt_card = stack[dealt_card_index]
    your_hand.append(dealt_card)
    stack.remove(dealt_card)


print("You've been dealt the following cards: ", ' <> '.join(your_hand))
#print("\nWhat remains: ", hearts)
#print(your_hand)
