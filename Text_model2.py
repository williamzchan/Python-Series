
# Text Models

import math

def clean_text(txt):
    """ processes each word in a text individually without worrying about punctuation or special characters """   
    text = txt.lower().split()
    listo = []
    
    for word in range(len(text)):
        
        if '!' in text[word]:
            new = text[word].replace('!', '')
            listo += [new]
        elif '.' in text[word] :
            new = text[word].replace('.', '')
            listo += [new]
        elif ',' in text[word]:
            new = text[word].replace(',', '')
            listo += [new]
        elif '?' in text[word]:
            new = text[word].replace('?', '')
            listo += [new]
        elif ';' in text[word]:
            new = text[word].replace(';', '')
            listo += [new]
        elif ':' in text[word]:
            new = text[word].replace(':', '')
            listo += [new]
        elif '"' in text[word]:
            new = text[word].replace('"', '')
            listo += [new]
        else:
            listo += [text[word]]
            
    return listo


def stem(s):
    """ returns the stem of an inputted string 's' """
    
    s.lower()
    
    if len(s) >= 2:
        
        if s[-1] == 'y':
            s = s[:-1]
            
        if s[-1] == 's':
            s = s[0:-1] 
            
        if s[-2:] == 'ed':
            
            s = s[:-2] 
            
        if s[-3:] == 'ing':
            
            s = s[0:-3]
    
            
    
        
        if s[:2] == 'un':
            
            s = s[2:] 
            
        if s[:2] == 're':
            
            s = s[2:]
            
        if s[:2] == 'bi':
            
            s = s[2:]        
        
        else:
            s = s[:]
            
        return s
    
    else:
        
            
        return s
    
def compare_dictionaries(d1, d2):
    
    """ returns the log similarity score of two dictionaries """
    

    score = 0
    total = 0
    
    for keys in d1:
        total += d1[keys]
        
    for value in d2:
        
        if value in d1:
            score += d2[value] * math.log(d1[value] / total)
        else:
            score += d2[value] * math.log(0.5 / total)
    return score
    


            
        
  

class TextModel:
    """ serves as a blueprint for objects that model a body of text """
    
    def __init__(self, model_name):
        """ constructs a new "TextModel' object by accepting a string 'model_name'
        and initializing three attributes """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuation_counter = {}
        
            
            
            
    def __repr__(self):
        """ returns a string representation of the 'TextModel' """
        
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n' + \
            '  number of word lengths: ' + str(len(self.word_lengths)) + '\n' + \
            '  number of stems: ' + str(len(self.stems)) + '\n' + \
            '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n' + \
            '  number of punctuations: ' + str(len(self.punctuation_counter)) 
        return s
    
    
    def add_string(self, s):
        """ analyzes the string 'txt' and adds its pieces to all dictionariesin this text model """
        
        count_length = 0
        words = s.lower().split()
        for A in words:
            
            count_length += 1
            if '?' in A or '.' in A or '!' in A :
                
                if count_length not in self.sentence_lengths:

                    self.sentence_lengths[count_length] = 1
                    count_length = 0
                    
                else:
                
                    self.sentence_lengths[count_length] += 1 
                    count_length = 0
                    
                    
        punk_count1 = 0
        punk_count2 = 0
        punk_count3 = 0
        for punctuation in words:
            
            if '!' in punctuation :
                punc = punctuation[-1]
                punk_count1 += 1
                self.punctuation_counter[punc] =  punk_count1
                
                
            if '.' in punctuation :
                punc = punctuation[-1]
                punk_count2 += 1
                self.punctuation_counter[punc] =  punk_count2
                
            if '?' in punctuation :
                punc = punctuation[-1]
                punk_count3 += 1
                self.punctuation_counter[punc] = punk_count3
                
   
        
        word_list = clean_text(s)
        
        for b in word_list :
        
            current_word = b
            
            if current_word not in self.words:
              
                self.words[b] = 1
         
            else: #if current_word is in d dictionary
                self.words[b] += 1
                
        for i in word_list:
            
            if len(i) not in self.word_lengths:
                self.word_lengths[len(i)] = 1
            else:
                self.word_lengths[len(i)] += 1
                
        for c in word_list :
        
            current_words = stem(c)
            
            if current_words not in self.stems:
              
                self.stems[current_words] = 1
         
            else: #if current_word is in d dictionary
            
                self.stems[current_words] += 1
        
               
    def add_file(self, filename):
        """adds all of the text in a file to the model"""
        file = open(filename, 'r', encoding='utf8', errors='ignore')
        text = file.read()
        file.close()            
        self.add_string(text)
        

    def save_model(self):  
        
        """A function that saves dictionary onto text file
        """
        
        f = open((self.name + '_' + 'words'), 'w')  
        f.write(str(self.words))
        f.close() 
        
        g = open((self.name + '_' + 'word_lengths'), 'w')
        g.write(str(self.word_lengths))
        g.close()
        
        h = open((self.name + '_' + 'stems'), 'w')
        h.write(str(self.stems))
        h.close()
        
        i = open((self.name + '_' + 'sentence_lengths'), 'w')
        i.write(str(self.sentence_lengths))
        i.close()
        
        j = open((self.name + '_' + 'punctuation_counter'), 'w')
        j.write(str(self.punctuation_counter))
        j.close()
    

    def read_model(self):
        
        """A function that demonstrates how to read a
        Python dictionary from a file.
        """
        f = open((self.name + '_' + 'words'), 'r')
        d_str1 = f.read()   
        f.close()
        
        g = open((self.name + '_' + 'word_lengths'), 'r')
        d_str2 = g.read()   
        g.close()
        
        h = open((self.name + '_' + 'stems'), 'r')
        d_str3 = h.read()   
        h.close()
        
        i = open((self.name + '_' + 'sentence_lengths'), 'r')
        d_str4 = i.read()   
        i.close()
        
        j = open((self.name + '_' + 'punctuation_counter'), 'r')
        d_str5 = j.read()   
        j.close()

        self.words = dict(eval(d_str1))      # Convert the string to a dictionary.
        self.word_lengths = dict(eval(d_str2))
        self.stems = dict(eval(d_str3))
        self.sentence_lengths = dict(eval(d_str4))
        self.punctuation_counter = dict(eval(d_str5))
 
    # pr4
    def similarity_scores(self, other):
        """ returns a list of log similarity scores, measuring the similarity of'self’ & ‘other’"""
        scores = []
        words = compare_dictionaries(other.words, self.words)

        word_lengths = compare_dictionaries(other.word_lengths, self.word_lengths)

        stem = compare_dictionaries(other.stems, self.stems)

        sentence_lengths = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)

        punctuation_counter = compare_dictionaries(other.punctuation_counter, self.punctuation_counter)


        scores += [words]
        scores += [word_lengths]
        scores += [stem]
        scores += [sentence_lengths]
        scores += [punctuation_counter]
        
        return scores

       
        
    def classify(self, source1,source2):

       scores1 = self.similarity_scores(source1)
       scores2 = self.similarity_scores(source2)


       print('scores for ' + 'source1' + ':'  +  str(scores1)  +  '\n' 
             + 'scores for '  + 'source2' + ':'  +  str(scores2)   )
       scores1_count = 0
       scores2_count = 0
       for i in range(len(scores1)):
            for j in range(len(scores2)):
                if scores1[i] > scores2[j]:
                    scores1_count += 1
                else:
                    scores2_count += 1
       if scores1_count > scores2_count:
           print('mystery is more likely to have come from source1')
       else:
           print('mystery is more likely to have come from source2')
           
        
                    
        
def test():
    """allows us to test our textmodel class """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
        
        
        
        
        
        
        
        
# Copy and paste the following function into finalproject.py
# at the bottom of the file, *outside* of the TextModel class.
def run_tests():
    """ tests to see which source our text files derives from"""
    source1 = TextModel('RickAndMorty')
    source1.add_file('Rick&Morty.txt')

    source2 = TextModel('RegularShow')
    source2.add_file('RegularShow.txt')

    new1 = TextModel('FamilyGuy')
    new1.add_file('FamilyGuy.txt')
    new1.classify(source1, source2)

    # Add code for three other new models below.        
        
    new2 = TextModel('Futurerama')
    new2.add_file('Futurerama.txt')
    new2.classify(source1, source2)
        
    new3 = TextModel('HarleyQuinn')
    new3.add_file('HarleyQuinn.txt')
    new3.classify(source1, source2)

    new4 = TextModel('RobotChicken')
    new4.add_file('RobotChicken.txt')
    new4.classify(source1, source2)    
            
