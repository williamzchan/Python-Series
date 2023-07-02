'loop practice' 


# problem 1
def log(b, n):
    """ finds the logarithm of 'n' with 'b' being the base """
    result = n
    counter = 0
    holder = result
   
    while holder > 1  :
        
        
        holder = result // b
        print('dividing', result, 'by', b, 'gives', holder)
        result = holder
        
        counter += 1
        
    return counter

# problem 2
def add_powers(m, n):
    """ it takes 'n' as the base and take the power of the base to 'm - 1 and adds up all the outputs of each 'power of' together """
    result = 0
    counter = 0
    holder = 0
    while counter < m :
        result =  n ** counter 
        print(n, '**', counter, '=', result)       
        counter += 1
        holder += result
        
    return holder

    

# problem 3    
def square_evens(values):
    """ Squares the even numbers in the given list and leaves the odds the same, but there's a catch it must change the list on a global scale """
    for i in range(len(values)) :
        if values[i] % 2 == 0 :
            values[i] *= values[i]            
    
