'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
def combine_dictionaries(dictionary_one, dictionary_two):
    '''
    create a combine dictionary of two dictionaries
    '''
    dictionary = {}
    for word in dictionary_one:
        if word in dictionary_two:
            if word not in dictionary:
                dictionary[word] = [dictionary_one[word], dictionary_two[word]]
    for word in dictionary_one:
        if word not in dictionary:
            dictionary[word] = [dictionary_one[word], 0]
    for word in dictionary_two:
        if word not in dictionary:
            dictionary[word] = [0, dictionary_two[word]]
    return dictionary

def calculate_similarity(dictionary):
    '''
    calculate the similarity
    '''
    numerator = sum([k[0] * k[1] for k in dictionary.values()])
    var_d1 = math.sqrt(sum([k[0] ** 2 for k in dictionary.values()]))
    var_d2 = math.sqrt(sum([k[1] ** 2 for k in dictionary.values()]))
    return numerator/(var_d1*var_d2)


def create_dictionary(words_list):
    '''
    returns a dictionary without stopwords
    '''
    dictionary = {}
    stopwords_doc = load_stopwords("stopwords.txt")
    for word in words_list:
        word = word.strip()
        if word not in stopwords_doc and word != "":
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary


def clean_given_text(text_input):
    '''
    clean the input text
    '''
    words = text_input.lower().strip().replace("\'", "")
    regex = re.compile('[^a-z]')
    words = regex.sub(" ", words).split(" ")
    return words


def similarity(text_input_one, text_input_two):
    '''
        Compute the document distance as given in the PDF
    '''
    # dict1.lower()
    # dict2.lower()
    dictionary_one = create_dictionary(clean_given_text(text_input_one))
    dictionary_two = create_dictionary(clean_given_text(text_input_two))
    dictionary = combine_dictionaries(dictionary_one, dictionary_two)
    return calculate_similarity(dictionary)

def load_stopwords(filename):
    '''
     loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename1:
        for line in filename1:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
    take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
