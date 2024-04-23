import random as r

# deal mechanism
def deal(player_h, dealer_h, deck):
    """
    Function that deals cards to the player and the dealer
    :param player_h: the players hand (list object)
    :param dealer_h: the dealers hand (list object)
    :param deck: the deck of cards we have (list object)
    :return: returns the player and dealer hands with two cards for each
    """
    for i in range(0, 2):
        player_h.append(r.choice(deck))
        dealer_h.append(r.choice(deck))
    return player_h, dealer_h


def hit(hand, deck):
    """
    Function that will add another card to the persons (player or dealer) hand
    :param hand: the player or the dealer as passed
    :param deck: the deck of cards (list object)
    :return: the updated hand of cards
    """
    hand.append(r.choice(deck))
    # hand.append(11) #test line
    return hand


def check_hand(hand):
    """
    Checks to see the value of the hand
    :param hand: the hand we want to check the value of
    :return: the score/value of the hand
    """
    total = 0
    for i in hand:
        total += i
    return total
