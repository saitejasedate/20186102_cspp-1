'''
@author : saitejasedate
# Exercise: Assignment-2
# Write a Python function, sumof_digts, that takes in one number
and returns the sum of digits of given number.

# This function takes in one number and returns one number.
'''

def sumofdigts(n_s):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n_s == 0:
        return 0
    return (n_s%10) + sumofdigts(n_s//10)


def main():
    '''
    Python function, sumof_digts, that takes in one number
    and returns the sum of digits of given number.
    '''
    a_s = input()
    print(sumofdigts(int(a_s)))

if __name__ == "__main__":
    main()
