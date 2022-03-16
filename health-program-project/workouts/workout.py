"""
This module holds the Workout class. This object stores a workout_log in the form of a dictionary, exercises, duration of the workout as length and measure of duaration as length_type. Each instance of the class is appended to the dictionary as value to todays date (key). This class can also has the funcitonality to design a workout based off the attributes given in the initializer, as well as adding additional exercises to the preset exercise list
"""

from datetime import datetime
from time import gmtime, strftime
import os
clear = lambda: os.system('clear') #This line creates a clear function to clear console as user iterates through menu options


class Workout:
    
    workout_log = {}
    exercises = None

    def __init__(self,length_type, length):
        self.date = datetime.today().strftime('%m-%d-%Y') #Workout instances will be logged by date
        self.workout_type = None #Workout_type is determined by child classes in other modules
        self.length_type = length_type #How user will measure workout. Either by Time or Reps
        self.length = length #length is how many reps or minutes the workout will be
        
       
        if length_type not in ('Reps','Time'):  #Error Handling for invalid
            raise ValueError('Are you training by number of repetitions or a time goal? Please enter Reps or Time.')
    
    
    #Method that willuse a classes exercises list create a workout determined by an instance length and length type attributes 
    def create_workout(self):
        exercises = self.exercises
        if exercises is not None:
            if self.length_type == 'Time':
                clear()
                print('For {} uninterupted minutes repeat the circuit below: \n '.format(self.length))
                for item in exercises :
                    print('8 x {}'.format(item))
            else:
                clear()
                print('\nComplete this circuit 4 times : \n ')
                for item in exercises:
                    print('{} x {} \n '.format(self.length, item))

            complete = input('Did you complete the workout?: ')
            if complete in ('Yes', 'yes'):
                if self.date not in Workout.workout_log.keys():
                    Workout.workout_log[self.date] = []
                    Workout.workout_log[self.date].append(self.workout_type)
                else:
                    Workout.workout_log[self.date].append(self.workout_type) 
        return
    
    #Method to see workout log
    def get_log():
        return Workout.workout_log
    
    #Method to log workout not in workout log
    def log_workout(self):
        if self.date not in Workout.workout_log.keys():
            Workout.workout_log[self.date] = []
            Workout.workout_log[self.date].append(self.workout_type)
        else:
            Workout.workout_log[self.date].append(self.workout_type) 
        return 'Workout has been recorded!'
    
    #Method that add new exercises to the child class exercises list
    def add_workout(cls,exercise):
        if exercise not in cls.exercises:
            cls.exercises.append(exercise)
            print('Exercise has been added to chosen catalog.')
        else:
            print('{} is already in the catalog'.format(exercise))
        return

   