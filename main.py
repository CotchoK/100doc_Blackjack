################# BLACKJACK PROJECT ###################

# deck unlimited in size
# there are no jokers
# Jack/Queen/King all valued at 10
# ace can count as 11 or 1

# the cards in the list have equal probability of being drawn
# cards are not removed from the deck as they are drawn.

# start the game
# cycle deal 1 card to player and one unknown c ard to dealer (face down)
# , deal next card to player and known (face up card to dealer)

# ask whether player wants to hit or stand
# if over 21 and an 11 is included (convert to 1)
# if over 21 then lose
# if under 21 and stand, dealer deal

########################################################

#import scripts
import actions as act
import ascii_art as aa

## using the following list of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# print logo
print(aa.logo)

# define player and dealer hands
player_hand = []
dealer_hand = []

# test hands
# player_hand = [10, 10]
# dealer_hand = [11, 11]

# gameplay handling variables
round_end = False
game_end = False
round_start = True
player_stand = False

# check to see if game is ended
while not game_end:
    # while the round has not ended execute the game loop
    while not round_end:
        # if it is the start of the game then let's deal cards and update round_start flag to false
        if round_start:
            act.deal(player_hand, dealer_hand, cards)
            round_start = False

        # calculate value of both player and dealer hand
        player_hand_value = act.check_hand(player_hand)
        dealer_hand_value = act.check_hand(dealer_hand)

        # print out the player hand and value and the dealer partial hand
        print(f"player hand: {player_hand} | value: {player_hand_value}")
        print(f"dealer hand: [#, {', '.join(map(str, dealer_hand[1:]))}]")

        # check if the player stands
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

        # if the player stands, then execute dealer based logic and win/lose conditions
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

        if round_end:
            # for testing purposes
            print(f"\ndealer hand: {dealer_hand} | value: {dealer_hand_value}")

            # check if the player wants to play again
            game_response = input("Would you like to play again? ('y' for yes, 'n' for no): ")
            # if the player doesn't want to play again exit the program.
            if game_response == 'n':
                exit()
            # if the player wants to play again reset all game objects to default
            else:
                round_start = True
                round_end = False
                player_stand = False
                player_hand.clear()
                dealer_hand.clear()
                print("\n")

# troubleshooting














