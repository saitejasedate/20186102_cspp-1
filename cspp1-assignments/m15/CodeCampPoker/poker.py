'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

GLOBAL_DICT = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2,\

     '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    # hand = []
    # for var_h in hand:
    #     hand.append(card_values[var_h[0]])
    # #print(hand)
    # hand.sort()
    # #flag=0
    for i in range(0, len(hand)-1):
        if hand[i+1] - hand[i] != 1:
            return False
    return True

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    suit = hand[0]
    for var_h in hand:
        if suit != var_h:
            return False
    return True

def is_four_a_kind(hand):
    '''
    If four cards in a hand are same returns true
    '''
    for i in range(len(hand)-3):
        if hand[i] == hand[i+1] == hand[i+2] == hand[i+3]:
            return True

def is_three_a_kind(hand):
    '''
    If three cards in a hand are same returns true
    '''
    for i in range(len(hand)-2):
        if hand[i] == hand[i+1] == hand[i+2]:
            return True
        return False

def is_one_pair(hand):
    '''
    If there is a pair of some cards in a hand returns true
    '''
    if len(hand) - len(set(hand)) == 1:
        return True
    return False

def is_two_pair(hand):
    '''
    If there are two pairs of same card in a hand returns true
    '''
    if len(hand) - len(set(hand)) == 2:
        return True
    return False



def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    face_hand = []
    suit_hand = []
    for i in hand:
        face_hand.append(GLOBAL_DICT[i[0]])
        suit_hand.append(i[1])
    face_hand.sort()
    suit_hand.sort()
    a_temp=[]
    card_rank = ['--23456789JQKA'.index(c) for c, s in hand]
    card_rank.sort()
    card_rank.reverse()
    if is_straight(face_hand) and is_flush(suit_hand):
        return (8, card_rank)
    elif is_four_a_kind(face_hand):
        return (4, card_rank)
    elif is_three_a_kind(hand) and is_one_pair(hand):
        return (7, card_rank)
    elif is_flush(suit_hand):
        return (6, card_rank)
    elif is_straight(face_hand):
        return (5, card_rank)
    elif is_three_a_kind(face_hand):
        return (3, card_rank)
    elif is_two_pair(face_hand):
        return (2, card_rank)
    elif is_one_pair(face_hand):
        for i in range(len(card_rank)-1):
            if card_rank[i] == card_rank[i+1]:
                a_temp = card_rank[i]
                card_rank = []
                card_rank.append(a_temp)
                break
        return (1, card_rank)
    return 0

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    #print (HANDS)

        # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
    #for h in HANDS:
        #print(is_straight(h))
