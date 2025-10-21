import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


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


while True:
    player_hand = [random.choice(cards), random.choice(cards)]
    dealer_hand = [random.choice(cards), random.choice(cards)]

    player_sum = calculate_sum(player_hand)
    dealer_sum = calculate_sum(dealer_hand)

    print("Player hand:", player_hand)
    print("Dealer hand: ['?',", dealer_hand[1], "]")

    # Проверка за Blackjack веднага след първите две карти
    if player_sum == 21:
        print("Player hits Blackjack! Player wins!")
        play_again = input("Do you want to play again? (Yes/No) ")
        if play_again.lower() != "yes":
            break
        else:
            continue
    elif dealer_sum == 21:
        print("Dealer hits Blackjack! Dealer wins!")
        play_again = input("Do you want to play again? (Yes/No) ")
        if play_again.lower() != "yes":
            break
        else:
            continue

    # Играч избира Hit или Stand
    while True:
        answer = input("Hit or Stand? ")
        if answer.lower() == "hit":
            player_hand.append(random.choice(cards))
            player_sum = calculate_sum(player_hand)
            print("Player hand:", player_hand)
            if player_sum > 21:
                print("Player busts!")
                break
            elif player_sum == 21:
                print("Player hits Blackjack! Player wins!")
                break
        else:
            break

    # Дилър тегли карти докато не достигне минимум 17
    while dealer_sum < 17:
        dealer_hand.append(random.choice(cards))
        dealer_sum = calculate_sum(dealer_hand)

    print("Final Player hand:", player_hand, "Sum:", player_sum)
    print("Final Dealer hand:", dealer_hand, "Sum:", dealer_sum)

    # Проверка кой печели
    if player_sum > 21:
        print("Player busts!")
    elif dealer_sum > 21:
        print("Dealer busts!")
    elif player_sum > dealer_sum:
        print("Player wins!")
    elif dealer_sum > player_sum:
        print("Dealer wins!")
    else:
        print("Draw!")

    # Въпрос за нова игра
    play_again = input("Do you want to play again? (Yes/No) ")
    if play_again.lower() != "yes":
        break
