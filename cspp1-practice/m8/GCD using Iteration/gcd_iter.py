# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    if a==0 or b==0:
        return 0
    elif a==1 or b==1:
        return 1
    else:
        count = 0
        maxn=max(a,b)
        for i in range(1,maxn):
            if a%i==0 and b%i==0:
                count = i
        return count 

def main():
    data = input()
    data = data.split()
    print(gcdIter(int(data[0]),int(data[1]))) 

if __name__ == "__main__":
    main()