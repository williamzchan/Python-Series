
# Markov Chain dictionary


import random


def create_dictionary(filename):
    """ creates a dictonary from a text file"""
    file = open(filename, 'r')
    text = file.read()
    words = text.split()
    file.close()
    d = {}
    current_word = '$'
    print('this is', words)
    for next_word in words :
        if current_word not in d:
            d[current_word] = [next_word]
            current_word = next_word
        else: #if current_word is in d dictionary
            d[current_word] += [next_word]
            current_word = next_word
        # update current_word to be either next_word or '$'
        if '!' in next_word or '.' in next_word or '?' in next_word :
            current_word = '$'
    
    return d





def generate_text(word_dict, num_words): #file , value
    """ Generates a random new sentence from the words of a text file"""
    current_word = '$'
    
    
    for i in range(num_words):
        
        
        next_word = random.choice(word_dict[current_word])
        
        
        print(next_word, end=' ')
        
        if next_word in word_dict:
            current_word = next_word
        else:
            current_word = '$'
        # update current_word to be either net_word or '$'
        
