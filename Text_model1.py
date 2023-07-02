
# Text Models

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


    
class TextModel:
    """ serves as a blueprint for objects that model a body of text """
    
    def __init__(self, model_name):
        """ constructs a new "TextModel' object by accepting a string 'model_name'
        and initializing three attributes """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        
    def __repr__(self):
        """ returns a string representation of the 'TextModel' """
        
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n' + \
            '  number of word lengths: ' + str(len(self.word_lengths))
        return s
    
    def add_string(self, s):
        """ analyzes the string 'txt' and adds its pieces to all dictionariesin this text model """
        word_list = clean_text(s)
        
        for w in word_list :
        
            current_word = w
            
            if current_word not in self.words:
              
                self.words[w] = 1
         
            else: #if current_word is in d dictionary
                self.words[w] += 1
        for i in word_list:
            
            if len(i) not in self.word_lengths:
                self.word_lengths[len(i)] = 1
            else:
                self.word_lengths[len(i)] += 1
              
               
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
        
                               
    

    def read_model(self):
        
        """A function that demonstrates how to read a
        Python dictionary from a file.
        """
        f = open((self.name + '_' + 'words'), 'r')
        d_str1 = f.read()   
        f.close()
        
        g= open((self.name + '_' + 'word_lengths'), 'r')
        d_str2 = g.read()   
        g.close()

        self.words = dict(eval(d_str1))      # Convert the string to a dictionary.
        self.word_lengths = dict(eval(d_str2))
