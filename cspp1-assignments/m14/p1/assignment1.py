'''Problem 1 - Build the Shift Dictionary and Apply Shift'''
# The Message class contains methods that could be used to apply a
# cipher to a string, either to encrypt or to decrypt a message
# (since for Caesar codes this is the same action).

# In the next two questions, you will fill in the methods of the
# Message class found in ps6.py according to the specifications in the
# docstrings. The methods in the Message class already filled in are:
# __init__(self, text)
# The getter method get_message_text(self)
# The getter method get_valid_words(self), notice that this one
# returns a copy of self.valid_words to prevent someone from mutating the
# original list.

# In this problem, you will fill in two methods:
# Fill in the build_shift_dict(self, shift) method of the Message class.
# Be sure that your dictionary includes both lower and upper case
# letters, but that the shifted character for a lower case letter and its
# uppercase version are lower and upper case instances of the
# same letter. What this means is that if the original letter is "a" and
# its shifted value is "c", the letter "A" should shift to the letter "C".

# If you are unfamiliar with the ordering or characters of the English alphabet,
# we will be following the letter ordering displayed by
# string.ascii_lowercase and string.ascii_uppercase:

# >>> import string
# >>> print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
# >>> print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# A reminder from the introduction page - characters such as the space character,
# commas, periods, exclamation points, etc will not be encrypted by this cipher
# Basically, all the characters within string.punctuation, plus the space (' ')
# and all numerical characters (0 - 9) found in string.digits.

# Fill in the apply_shift(self, shift) method of the Message class.
# You may find it easier to use build_shift_dict(self, shift).
# Remember that spaces and punctuation should not be changed by the cipher.

# Helper code
import string
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    in_file.close()
    return word_list

WORDLIST_FILENAME = 'words.txt'
# Helper code End


### Paste your implementation of the Message class here
class Message():
    '''
    message
    '''
    def __init__(self, text):
        '''
        constructor
        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")
        self.shift_dict = {}
    def get_message_text(self):
        '''
        message getter
        '''
        return self.message_text
    def get_valid_words(self):
        '''
        valid words
        '''
        return self.valid_words[:]
    def build_shift_dict(self, shift):
        '''
        letters of string
        '''
        lower_keys = list(string.ascii_lowercase)
        lower_values = list(string.ascii_lowercase)
        shift_lower_vals = lower_values[shift:] + lower_values[:shift]
        upper_keys = list(string.ascii_uppercase)
        upper_values = list(string.ascii_uppercase)
        shift_upper_vals = upper_values[shift:] + upper_values[:shift]
        total_keys = lower_keys + upper_keys
        total_values = shift_lower_vals + shift_upper_vals
        self.shift_dict = dict(zip(total_keys, total_values))
        return self.shift_dict
    def apply_shift(self, shift):
        '''
        shift strings
        '''
        new_msg = []
        for i in self.message_text:
            if i not in self.build_shift_dict(shift).keys():
                new_msg.append(i)
                continue
            else:
                new_msg.append(self.build_shift_dict(shift)[i])
        return ''.join(new_msg)




    # def get_message_text(self):
    #     return self.

def main():
    '''
        Function to handle testcases
    '''
    data = Message(input())
    data.get_message_text()
    print(data.apply_shift(int(input())))

if __name__ == "__main__":
    main()
