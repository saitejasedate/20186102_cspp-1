'''
@author : saitejasedate
'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial_num(n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if n==0:
        return 1
    return n*factorial_num(n-1)
    
    
    


def main():
    a = input()
    print(factorial_num(int(a)))

if __name__ == "__main__":
    main()
