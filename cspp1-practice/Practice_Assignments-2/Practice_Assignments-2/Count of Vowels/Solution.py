'''
program that return True whether the given string has
more number of vowels than consonants, otherwise return False.
'''
vowels_str = "aeiou"

def count_vowels(string_input):
	'''
	returns number of vowels in the given string parameter.
	'''
	cou_nt=0
	for letter in string_input:
		if letter in vowels_str:
			cou_nt += 1
	return cou_nt	


def count_consonants(string_input):
	'''
	returns number of consonants in the given string parameter.
	'''
	cou_nt1=0
	for letter in string_input:
		if letter not in vowels_str:
			cou_nt1 += 1
	return cou_nt1	


def is_vowels_count_higher(string_input):
	'''
	returns true if vowels count is greater than consonants count, otherwise false
	'''
	return count_vowels(string_input) > count_consonants(string_input)


def main():
	string_input = input()
	print(is_vowels_count_higher(string_input))

main()