#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	s=input()
	# the input string is in s
	# remove pass and start your code here
	vowels="a, e, i, o, u"
	b=len(vowels)
	l=len(s)
	c=0
	j=0
	for i in range(0,l,1):
		for j in range(0,b,1):
			if s[i]==vowels[j]:
				c=c+1
	print(c)

if __name__ == "__main__":
	main()
