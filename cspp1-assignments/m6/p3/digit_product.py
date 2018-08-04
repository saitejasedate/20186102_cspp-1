'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    a=list(str(int_input))
    l=len(a)
    temp=1
    c=0
    while c!=l:
    	rem=int_input%10
    	temp=temp*rem
    	c=c+1
    	mod=int_input//10
    	int_input=mod
    print(temp)


if __name__ == "__main__":
    main()
