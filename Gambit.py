import random

hand = []

discard = []

deck = ["Chaos_Bolt","Chaos_Bolt","Chaos_Bolt",
        "Ice_Knife","Ice_Knife","Ice_Knife",
        "Witch_Bolt","Witch_Bolt","Witch_Bolt",
        "Melfs_Minute_Meteors",
        "Conjure_Animals",
        "Cryostasis",
        "Scorching_Ray",
        "Mirror_Image",
        "Shield","Shield","Shield",
        "Wildcard","Wildcard","Wildcard"]

#Output Remaining hand and Discard pile        
def output():
    print("\nHand of Fate", hand)
    print("Discard Pile", discard, "\n")
    choice()
    
#Enhance the level of a spell by discarding
def enhance():
    print ("Enhance")
    print (hand)
 #Get the index and discard the card
    disc = int(input("\nEnter the index to increase spell level:\t"))
    discard.append(hand[disc])
    del hand[disc]
 #Output remaining hand
    output()

#Cast a spell and/or enhance it
def cast_spell():
    print ("Cast Spell")
    print (hand)
 #Choose a spell to cast and discards it
    spell = int(input("\nWhat spell do you want to cast?\t"))
    discard.append(hand[spell])
    del hand[spell]
 #Choose to enhance the spell or not
    enh = input("Would you like to enhance this spell? (y/n)\t")
    if enh == "y":
        enhance()
    elif enh == "n":
        output()
            
#Discard a card and cast the card throw cantrip
def card_throw():
    print(hand)
 #Get the index and discard the card
    index = int(input("\nChoose a card to throw then shuffle it into the deck:\t"))
    deck.append(hand[index])
    del hand[index]
 #Roll for a color
    color = random.randint(1,6)
    print("Card Throw, ", color)
 #Determine the damage type
    if color == 1:
        print("Red")
        print("Fire")
    elif color == 2:
        print("Orange")
        print("Acid")
    elif color == 3:
        print("Yellow")
        print("Lightning")
    elif color == 4:
        print("Green")
        print("Poison")
    elif color == 5:
        print("Blue")
        print("Cold")
    elif color == 6:
        print("Violet")
        print("Psychic")
    output()

#Discard a card and draw a new one
def cycling():
    print ("Cycling")
    print (hand)
 #Get the index and discard the card
    index = int(input("\nEnter the index to discard and draw a new one:\t"))
    discard.append(hand[index])
    del hand[index]
 #Get the new card
    new = random.choice(deck)
    print("Card drawn: ", new)
    hand.append(new)
    deck.remove(new)
 #Output hand with new card
    output()
    
#Once per short rest, move cards from your discard to your deck
def full_house():
    f = 0
    print("Full House")
    while f < 5:
        print(discard)
        card = int(input("\nEnter the index of the card you want to restore: \t"))
        deck.append(discard[card])
        del discard[card]
        f += 1
    output()

#Draw 5 cards into your hand
def draw_hand():
    d = 0
    print ("Draw Hand\n")
 #Draw 5 cards
    while d < 5:
     draw = random.choice(deck)
     print (draw)
     hand.append(draw)
     deck.remove(draw)
     d += 1
 #Prompt next choice
    print()
    choice()

#Shuffle hand into deck and redraw    
def mulligan():
 #Shuffle hand into deck
    deck.extend(hand)
    hand.clear()
 #Draw a new hand
    h = 0
    print ("Mulligan Hand\n")
 #Draw 5 cards
    while h < 4:
     draw = random.choice(deck)
     print (draw)
     hand.append(draw)
     deck.remove(draw)
     h += 1
 #Prompt next choice
    print()
    choice()
    
#Choose a card to possess for 1 minute
def one_with_the_card():
    print("One with the Card")
    print(hand)
 #Choose a card to use
    bond = int(input("Choose a card to bond to for 1 min \t"))
    discard.append(hand[bond])
    del hand[bond]
    print("\nAnimate your card and move 30ft:")
    print("See and hear through the card or as a bon act, teleport to that space")
 #Output the choice
    output()
 
print("Welcome to Hands of Fate:\n")

def choice():
    print("\t1: Draw Hand \t2: Cast Spell \t3: Card Throw \t4: Cycling \
          \t\t5: Mulligan \t6: Full House \t7: One with the Cards \t8: Current Hand")
     
    option = input("Pick a card...any card\t")
    
    if option == "1":
        draw_hand()
    elif option == "2":
        cast_spell()
    elif option == "3":
        card_throw()
    elif option == "4":
        cycling()
    elif option == "5":
        mulligan()
    elif option == "6":
        full_house()
    elif option == "7":
        one_with_the_card()
    elif option == "8":
        output()

choice()




