'''
@author : saitejasedate
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number 
and returns the factorial of given number
# This function takes in one number and returns one number.
'''

def factorial_num(n_um):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n_um == 0:
        return 1
    return n_um*factorial_num(n_um-1)

def main():
    '''
    Python function, factorial(n), that takes in one number 
    and returns the factorial of given number
    '''
    a_n = input()
    print(factorial_num(int(a_n)))

if __name__ == "__main__":
    main()
