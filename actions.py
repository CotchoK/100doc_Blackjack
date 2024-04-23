import random as r

# deal mechanism
def deal(player_h, dealer_h, deck):
    for i in range(0, 2):
        player_h.append(r.choice(deck))
        dealer_h.append(r.choice(deck))
    return player_h, dealer_h


def hit(hand, deck):
    hand.append(r.choice(deck))
    # hand.append(11) #test line
    return hand


def check_hand(hand):
    total = 0
    for i in hand:
        total += i
    return total
