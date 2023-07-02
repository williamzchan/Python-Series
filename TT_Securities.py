''' python program that replicates a TT Security or just a bank transfer interface'''

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the median price')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.

# problem 1
def avg_price(prices):
    """ Finds teh mean of the list of prices"""
    result = 0
    mean = 0
    for x in prices:
        mean += x
        
        result += 1
    result = mean / result
    
    return result
 
    
# problem 2
def median_price(prices):
    """Finds the median price of the list of prices"""
    copy = prices[:]
    copy.sort()
    result = 0   
   
    if len(copy) % 2 == 1 :
        result = len(copy) // 2
        return copy[result]
    else: 
        result = len(copy) // 2
        
        return (copy[result - 1] + copy[result]) / 2 
   
    
# problem 3    
def max_day(prices):
    """ Finds the day with the max price within a list"""
    holder = prices[1]
    for i in range(len(prices)):
        if prices[i] > holder:
            holder = prices[i]
    for i in range(len(prices)):
        if prices[i] == holder:
            return i
        
        
 # problem 4           
def any_above(prices, threshold):
    """Finds if any of the prices inside a list of prices is within the threshold"""
    for x in prices:
        if x > threshold:
            return True
    else:
        return False 


# problem 5        
def find_tts(prices):
    """ Finds the best day to buy and best day to sell stocks for the most profit """
    constant = prices[0]
      
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            a = (prices[i] - prices[j])
            if a < constant:
                constant = a
                minimum = i
                maximum = j
                profit = prices[maximum] - prices[minimum]
            elif i == (len(prices)-1):
                
                return [minimum, maximum, profit]
                
                

def tts():
    """ the main user-interaction loop
    """
    prices = []
    threshold = []
    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            print('The average price is', avg_price(prices))
        elif choice == 4:
            print('The median price is', median_price(prices))
        elif choice == 5:
            hold = max_day(prices)
            print(' The max price is', prices[hold], 'on day', hold) #maybe not correc
        elif choice == 6:
            threshold = int(input('Enter the threshold: '))
            hold3 = any_above(prices, threshold)
            if hold3 == True:
                print('There is at least one price above', threshold)
            else:
                print('There are no prices above', threshold)
        elif choice == 7:
           hold2 = find_tts(prices)
           print('Buy on day', hold2[0], 'at price', prices[hold2[0]])
           print('Sell on day', hold2[1], 'at price', prices[hold2[1]]) 
           print('Total profit: ', hold2[2])
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
