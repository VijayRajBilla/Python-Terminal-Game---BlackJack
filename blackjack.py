import random

deck = [
    '2', '2', '2', '2',  
    '3', '3', '3', '3',  
    '4', '4', '4', '4',  
    '5', '5', '5', '5',  
    '6', '6', '6', '6',  
    '7', '7', '7', '7',  
    '8', '8', '8', '8',  
    '9', '9', '9', '9',  
    '10', '10', '10', '10',  
    'J', 'J', 'J', 'J',  
    'Q', 'Q', 'Q', 'Q',  
    'K', 'K', 'K', 'K',  
    'A', 'A', 'A', 'A'   
]


print("Welcome to the Python Blackjack Game!")
print("************************************")
print("Rules:")
print("1. The goal is to get as close to 21 as possible without exceeding it.")
print("2. Number cards (2-10) are worth their face value.")
print("3. Face cards (Jack, Queen, King) are worth 10.")
print("4. Aces can be worth 1 or 11, whichever is more beneficial for your hand.")
print("5. You can 'Hit to take another card or 'Stand' to keep your current hand.")
print("6. The dealer must hit until they reach a total of 17 or higher.")
print("************************************")
print("Let's get started! Good luck!!!")



random.shuffle(deck)



sump = 0
sumd = 0

def calculate_sum(sum, card):
    if (card == "K" or card == "Q" or card == "J"):
        sum += 10
    elif (card == "A"):
        if (sum <= 10):
            sum += 11
        else:
            sum += 1
    else:
        sum += int(card)
    return sum

player_cards = []
dealer_cards = []


def player_start_hand():
    global sump
    global player_cards
    first = deck.pop(0)
    second = deck.pop(1)
    print("\nYour cards: {}, {}".format(first, second))

    sump = calculate_sum(sump, first)
    sump = calculate_sum(sump, second)

    player_cards.append(first)
    player_cards.append(second)


def dealer_start_hand():
    global sumd
    global dealer_cards
    one = deck.pop(0)
    two = deck.pop(0)
    print("\nDealer's cards: {}, [hidden]".format(one))
    
    sumd = calculate_sum(sumd, one)
    sumd = calculate_sum(sumd, two)

    dealer_cards.append(one)
    dealer_cards.append(two)

print("\nCards are being dealt to you and the dealer......")
player_start_hand()
dealer_start_hand()

print("\nYour total: " + str(sump))


def workp():
    global sump
    global player_cards
    while True:
        print("\nIt's your turn player.")
        print("What would you like to do?")
        print("\nPress 1 to hit and 2 to stand")
        action = input()
        if action == "1":
            card = deck.pop(0)
            print("\nYour next card is " + card)
            player_cards.append(card)
            print("\nYour cards: ")
            print(player_cards)
            sump = calculate_sum(sump, card)
            print("\nYour new total is " + str(sump))
            if sump > 21:
                print("So, this means you have gone bust and lost the game.")
                print("The Dealer wins.")
                return False
            return True
        if action == "2":
            print("You have opted to stand out with a total of " + str(sump))
            return True

def workd():
    global dealer_cards
    global sumd
    print("\nIt's now the Dealer's turn....")
    print("\nDealer draws a card")
    while sumd <= 17:
        card = deck.pop(0)
        sumd = calculate_sum(sumd, card)
        dealer_cards.append(card)
    if sumd > 21:
        print("\nThe dealer's sum exceeds 21.")
        print("\nDealer's cards: ")
        print(dealer_cards)
        print("\nDealer goes bust")
        print("\nSo, you are the winner!!")
    elif sumd > sump:
        print("\nThe dealer wins with a higher total than the player.")
        print("\nYour total is " + str(sump))
        print("\nDealer's cards: ")
        print(dealer_cards)
        print("\nThe dealer's total is " + str(sumd))
        print("\nYou have lost.")
    else:
        print("\nThe player wins with a higher total than the dealer.")
        print("\nYour total is " + str(sump))
        print("\nDealer's cards: ")
        print(dealer_cards)
        print("\nThe dealer's total is " + str(sumd))
        print("\nHooray!!! You have won")

while True:
    if not workp():
        break
    workd()
    if sumd > 21 or sumd >= 17:
        break

