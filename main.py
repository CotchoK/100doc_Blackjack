################# BLACKJACK PROJECT ###################

# deck unlimited in size
# there are no jokers
# Jack/Queen/King all valued at 10
# ace can count as 11 or 1
## using the following list of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# the cards in the list have equal probability of being drawn
# cards are not removed from the deck as they are drawn.

# start the game
# cycle deal 1 card to player and one unknown c ard to dealer (face down)
# , deal next card to player and known (face up card to dealer)

# ask whether player wants to hit or stand
# if over 21 and an 11 is included (convert to 1)
# if over 21 then lose
# if under 21 and stand, dealer deal

#import scripts
import actions as act

# define player and dealer hands
player_hand = []
dealer_hand = []

# test hands
# player_hand = [10, 10]
# dealer_hand = [11, 11]

round_end = False
round_start = True
player_stand = False

while not round_end:
    if round_start:
        #act.deal(player_hand, dealer_hand, cards)
        round_start = False

    player_hand_value = act.check_hand(player_hand)
    dealer_hand_value = act.check_hand(dealer_hand)

    print(f"player hand: {player_hand} | value: {player_hand_value}")
    print(f"dealer hand: {dealer_hand} | value: {dealer_hand_value}")

    if not player_stand:
        if player_hand_value == 21:
            player_stand = True
        elif player_hand_value < 21:
            response = input("Would you like to 'hit' or 'stand'? ") # ask to hit or stand
            if response == 'hit':
                act.hit(player_hand, cards)
            elif response == 'stand':
                player_stand = True
        elif player_hand_value > 21:
            if 11 in player_hand:
                player_hand[player_hand.index(11)] = 1
                print("you had an 11")
            else:
                print("You bust.")
                round_end = True

    if player_stand:
        if dealer_hand_value > 21:
            if 11 in dealer_hand:
                dealer_hand[dealer_hand.index(11)] = 1
                print("dealer had an 11")
            else:
                print("Dealer bust")
                round_end = True
        elif dealer_hand_value < 17:
            act.hit(dealer_hand, cards)
        elif dealer_hand_value == player_hand_value:
            print("It's a draw")
            round_end = True
        elif dealer_hand_value > player_hand_value:
            if dealer_hand_value == 21 and len(dealer_hand) == 2:
                print("Dealer wins. Dealer got blackjack")
            else:
                print("Dealer wins")
            round_end = True
        else:
            if player_hand_value == 21 and len(player_hand) == 2:
                print("You win. You got blackjack")
            else:
                print("You win")
            round_end = True





#player_hand, dealer_hand = deal(player_hand, dealer_hand, cards)


# print(player_hand)
# print(dealer_hand)
#
# hit(player_hand, cards)
# hit(dealer_hand, cards)
#
# print(player_hand)
# print(dealer_hand)











