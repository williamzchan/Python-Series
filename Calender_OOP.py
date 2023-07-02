
# Date Class



class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year

    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    #### Put your code for problem 2 below. ####
    #### Make sure that it is indented by an appropriate amount. ####
    # problem 3
    def advance_one(self):
        """ Finds one date ahead of given date"""
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if self.is_leap_year() == True:
            days_in_month[2] = 29
        
        if days_in_month[self.month] == 31:
            if self.month == 12 and self.day == 31:
                self.year += 1 
                self.month = 1
                self.day = 0
            if self.day < 31:
                self.day += 1
            if self.month != 12 and self.day == 31   :
                self.day = 1 
                self.month += 1
        if days_in_month[self.month] == 30:
            if self.day == 30:
                self.month += 1
                self.day = 0
            if self.day < 30 :
                self.day += 1
            
        if days_in_month[self.month] == 28:
            if self.day == 28:
                self.month += 1
                self.day = 0
            if self.day < 28:
                self.day += 1
        if days_in_month[self.month] == 29:
            if self.day == 29:
                self.month += 1
                self.day = 0
            if self.day < 29:
                self.day += 1
                
                
    # problem 4
    def advance_n(self, n):
        """ Finds 'n' date ahead of given date"""
        holder = n
        print(self)
        while holder > 0:
            
            self.advance_one()
            print(self)
            holder -= 1    
        
    #problem 5
    def __eq__(self, other):
        
        """ Finds whether the two given dates are equal to one another"""
        
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False
        
    # problem 6
    def is_before(self, other):
        
        """ Finds whether given is before new given date"""
        
        if self.year > other.year:
            return False
        elif self.year == other.year:
            if self.month > other.month:
                return False
            elif self.month == other.month:
                if self.day > other.day:
                    return False
                elif self.day == other.day:
                    return False
                else:
                    return True       
            else:
                return True 
        else:
            return True
        
    # problem 7
    def is_after(self, other):
        
        """ Finds whether given date is after new given date"""
        
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                if self.day > other.day:
                    return True
                else:
                    return False       
            else:
                return False 
        else:
            return False
        
    # problem 8
    def days_between(self, other):
       """Finds days between two dates""" 
       counter = 0
       
       

       if self.is_after(other) == True:
           copy_before = other.copy()
           copy_after = self.copy()
            
       if self.is_before(other) == True:
           copy_before = self.copy()
           copy_after = other.copy()
           
       elif self == other:
           return 0
       
       while copy_before != copy_after:
           copy_before.advance_one()
           counter += 1
    
       if self.is_before(other) == True:
           counter *= -1
           
       return counter
   
    # problem 9
            
    def day_name(self):
        day_names = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        date = 4/6/2041
        
        between = self.days_between(self, date)
        
       

            
            

            
