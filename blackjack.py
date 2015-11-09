import random
import time
values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    }
def win_check():
    if player_value == 21:
        return True
    elif player_value > 21:
        return False
def count_check(cards):
    #Check if a card is repeated 4 times
    tester = 0
    for i in cards:
        if cards.count(i) > 4:
            tester +=1
    if tester > 0:
        return True
    else:
        return False
card_list =  ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
def black_jack():
    play = "yes"
    player_hand = []
    dealer_hand = []
    current_cards = []
    print ("Welcome to BlackJack!")
    time.sleep(1)
    
    while play == "yes":
        
        #distributing cards
        print("Your starting cards are:")
        time.sleep(1)
        
        player_hand = [card_list[random.randint(0,12)],
                       card_list[random.randint(0,12)]]
        
        dealer_hand = [card_list[random.randint(0,12)],
                       card_list[random.randint(0,12)]]
        
        player_value_card1 = values[player_hand[0]]
        player_value_card2 = values[player_hand[1]]
        player_value = 0
        
        if (player_value_card1 == 1 or player_value_card2 == 1) and (player_value_card1 == 10 or player_value_card2 == 10):
            player_value = 21
            blackjack_player = True
        else:
            player_value = player_value_card1 + player_value_card2
            blackjack_player = False

        print(player_hand[0] + ", " + player_hand[1])
        print ("Your value is currently: ")
        time.sleep(1)
        print (player_value)
        time.sleep(1)

        dealer_value_card1 = values[dealer_hand[0]]
        dealer_value_card2 = values[dealer_hand[1]]
        dealer_value = 0

        #current card counter
        current_cards = [player_hand[0], player_hand[1],
                         dealer_hand[0], dealer_hand[1]]
        
        if (dealer_value_card1 == 1 or dealer_value_card2 == 1) and (dealer_value_card1 == 10 or dealer_value_card2 == 10):
            dealer_value = 21
            blackjack_dealer = True
        else:
           dealer_value = dealer_value_card1 + dealer_value_card2
           blackjack_dealer = False
           
        #player turn
        print("It is your turn")
        time.sleep(1)
        
        if player_value == 21:
            print("You already have 21!")
            
        else:
            while player_value < 21:
                draw = input("Would you like to draw? Yes/No ")
                while draw.lower() != "yes" and draw.lower() != "no":
                    draw = input("Oops! You have to enter Yes/No ")
                if draw.lower() == "yes":
                    print("You choose to draw!")
                    
                    card_draw = card_list[random.randint(0,12)]
                    current_cards.append(card_draw)
                    redraw = count_check(current_cards)
                    
                    while redraw == True:
                        current_cards.pop()
                        card_draw = card_list[random.randint(0,12)]
                        current_cards.append(card_draw)
                        redraw = count_check(current_cards)
                        
                    player_hand.append(card_draw)
                    player_value = player_value + values[card_draw]
                    
                    print("You drew: " + card_draw)
                    time.sleep(1)
                    print("Your current hand is... ")
                    
                    for i in player_hand:
                        print (i)
                    time.sleep(1)
                    print("Your value is currently... ")
                   
                    print(player_value)
                    time.sleep(1)

                    
                else:
                    print("You chose not to draw")
                    break
        if player_value > 21:
            time.sleep(1)
            print("You lose! Your value is greater than 21!")
            play = input("Play again? Yes/No ")
            if play == "no":
                break
            else:
                continue
            
            
        #dealer turn
        print("It's the dealer's turn")
        time.sleep(1)

        while dealer_value <= 16:
            print("The dealer chooses to draw!")

            card_draw = card_list[random.randint(0,12)]
            current_cards.append(card_draw)
            redraw = count_check(current_cards)
                    
            while redraw == True:
                current_cards.pop()
                card_draw = card_list[random.randint(0,12
                                                     )]
                current_cards.append(card_draw)
                redraw = count_check(current_cards)
                        
            dealer_hand.append(card_draw)
            dealer_value = dealer_value + values[card_draw]
            time.sleep(1)
        print("Time to compare!")
        time.sleep(2)
        if blackjack_dealer == True and blackjack_player == False:
            print("You lose! Dealer had blackjack! Tough luck!")
            time.sleep(2)
            play = input("Play again? Yes/No ")
        elif blackjack_player == True and blackjack_dealer == False:
            print("You win! You had blackjack!")
            time.sleep(2)
            play = input("Play again? Yes/No ")
        elif player_value > dealer_value and dealer_value < 21:
            print("Your value: ")
            print(player_value)
            time.sleep(1)
            print("is greater than the dealer's: ")
            print(dealer_value)
            time.sleep(1)
            print("You win!")
            play = input("Play again? Yes/No ")
        elif player_value < 21 and dealer_value > 21:
            print("Your value: ")
            print(player_value)
            time.sleep(1)
            print("Dealer's value: ")
            print(dealer_value)
            time.sleep(1)
            print("You win! The dealers cards valued over 21!")
            play = input("Play again? Yes/No ")
        elif player_value == dealer_value:
            print("Your value: ")
            print(player_value)
            time.sleep(1)
            print("is equal to the dealer's: ")
            print(dealer_value)
            time.sleep(1)
            print("You tie!")
            play = input("Play again? Yes/No ")
        else:
            print("Your value: ")
            print(player_value)
            time.sleep(1)
            print("is less than the dealer's: ")
            print(dealer_value)
            time.sleep(1)
            print("You lose!")
            play = input("Play again? Yes/No ")
black_jack()

