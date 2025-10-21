import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

player_hand = [random.choice(cards), random.choice(cards)]
dealer_hand = [random.choice(cards), random.choice(cards)]

player_hand.append(random.choice(cards))
dealer_hand.append(random.choice(cards))

print("Player hand:", player_hand)
print("Dealer hand:", dealer_hand)


def calculate_sum(hand):
    total = 0
    aces = 0
    for card in hand:
        if type(card) == int:
            total += card
        elif card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            total += 11
            aces += 1

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


player_sum = calculate_sum(player_hand)
dealer_sum = calculate_sum(dealer_hand)

while dealer_sum < 17:
    dealer_hand.append(random.choice(cards))
    dealer_sum = calculate_sum(dealer_hand)

print("Player sum:", player_sum)
print("Dealer sum:", dealer_sum)

if player_sum > 21:
    print("Player busts! Dealer wins!")
elif dealer_sum > 21:
    print("Dealer busts! Player wins!")
elif player_sum > dealer_sum:
    print("Player wins!")
elif dealer_sum > player_sum:
    print("Dealer wins!")
else:
    print("Draw!")
