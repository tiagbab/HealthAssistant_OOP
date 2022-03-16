"""The Core class is a child classes of Workout that inherits all of its attributes but has different class exercises variable."""

from workouts.workout import Workout

class Core(Workout):
   
    exercises = ['Side Crunches',
                          'Sit-Ups',
                          '30 Second Plank',
                          'V-Ups',
                          'Supermans',
                          'Shoulder Taps'
                         ]
    def __init__(self, length_type, length):
        Workout.__init__(self,length_type, length)
        self.workout_type = 'Core' #Workout_type is determined by child classes in other modules
        self.length_type = length_type #How user will measure workout. Either by Time or Reps
        self.length = length#length is how many reps or minutes the workout will be      

