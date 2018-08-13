'''
update the hand of the player
'''


def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    for letter in word:
        if letter in hand:
            hand[letter] = hand[letter] + 1
    return hand

def main():
    '''
    Main function
    '''
    n_int = input()
    adict = {}
    for i in range(int(n_int)):
        del i
        data = input()
        l_list = data.split()
        adict[l_list[0]] = int(l_list[1])
    data1 = input()
    print(update_hand(adict, data1))

if __name__ == "__main__":
    main()
