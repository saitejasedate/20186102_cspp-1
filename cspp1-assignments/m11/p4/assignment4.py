#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player.
'''
We'll be implementing the playHand function. This function allows the user to play out a
single hand. First, though, you'll need to implement the helper calculateHandlen function,
which can be done in under five lines of code.
'''

def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    sum_n = 0
    for iter_n in hand:
        sum_n = sum_n + hand[iter_n]
    return sum_n

def main():
    '''
     Returns the length (number of letters) in the current hand.
    '''
    n_var = input()
    adict = {}
    for i in range(int(n_var)):
        del i
        data = input()
        l_var = data.split()
        adict[l_var[0]] = int(l_var[1])
    print(calculate_handlen(adict))


if __name__ == "__main__":
    main()
