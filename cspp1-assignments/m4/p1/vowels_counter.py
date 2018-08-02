#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	s1=input()
	# the input string is in s
	# remove pass and start your code here
	s2="a, e, i, o, u"
	b=len(s2)
	l=len(s1)
	c=0
	j=0
	for i in range(0,l,1):
		for j in range(0,b,1):
			if s1[i]==s2[j]:
				c=c+1
	print(c)

if __name__ == "__main__":
	main()
