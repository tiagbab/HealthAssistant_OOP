"""
This module holds the Meal class. The Meal object stores a food, log and corresponding date stamp for each instance of this class. Each instance created takes in a food item, its calories and an optional comment. Every instance is added to the classes' log variable. This class also contains a method to retrieve food log dictionary.  
"""

from datetime import datetime
from time import gmtime, strftime
import os



#This line creates a clear function to clear console as user iterates through menu options
clear = lambda: os.system('clear')

#This code creates Meal class to log meals and calories
class Meal:
    
    food_log = {}
     
    def __init__(self, food, calories, comment='None'):
        self.date = datetime.today().strftime('%m-%d-%Y')
        self.food = food
        self.calories = calories
        self.comment = comment
        if self.date not in Meal.food_log.keys():
            Meal.food_log[self.date]  = []
            Meal.food_log[self.date].append((self.food, self.calories, self.comment))
        else:
            Meal.food_log[self.date].append((self.food, self.calories, self.comment))
    
    #method to retrieve food log class variable 
    def get_log():
        return Meal.food_log

#End of Meal Class