"""The HIIT class is a child classes of Workout that inherits all of its attributes but has different class exercises variable."""

from datetime import datetime
from time import gmtime, strftime
import os
from workouts.workout import Workout

class HIIT(Workout):
    exercises = ['Plyo Push-Ups',
                  'Russian Twists',
                  'Single-Leg Burpees',
                  'Supermans with Lateral Raises',
                  'Lateral Lunges with Hops',
                  'Tuck-Ups',
                  'Burpee',
                  'Mountain Climbers'
                ]
    def __init__(self, length_type, length):
        Workout.__init__(self,length_type, length)
        self.workout_type = 'HIIT' #Workout_type is determined by child classes in other modules
        self.length_type = length_type#How user will measure workout. Either by Time or Reps
        self.length = length #length is how many reps or minutes the workout will be
        
       
