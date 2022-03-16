"""
The HealthAssistant class pull together the functionality of all the other classes(Workout, HIIT, Core, Strength, Meal) in the program. The methods in this program take in user arguments to create class instances and the desired modifications to class variables.
"""

from datetime import datetime
from time import gmtime, strftime
import os
from workouts.workout import Workout
from workouts.hiit import HIIT
from workouts.core import Core
from workouts.strength import Strength
from meal.meal import Meal


clear = lambda: os.system('clear') #This line creates a clear function to clear console as user iterates through menu options


class HealthAssistant:
    
    all_actions = []
    
    def __init__():
        #self.action = int(input('What would you like to do? Please select a number: \n 1.Generate workout\n 2.Add to workout catalog\n 3.Log a meal \n 4.View activity log '))
        #self.action_id = strftime("%Y-%m-%d %H:%M:%S", gmtime())  #Creating a unique timestamp id for every self.action
        
        if action not in range(1,5):
            print('Invalid entry. Please enter corresponding number from menu.') #Error checking to ensure valid entry
        else:
            pass
    
    #This method gives user option to exit out of program or continue to select item
    def finish():
        done = input('Are you done with your health assistant?(yes/no): ')
        if done not in('Yes', 'yes','YES','No', 'no','NO'):
            print('Invalid entry. Please enter yes or no.')
            HealthAssistant.finish()
        elif done in ('Yes', 'yes','YES'):
            clear()
            print('Thanks for using the health assistant!')
        else:
            HealthAssistant.perform()
        
        return
    
    #This class method takes user input to create and log instance of desired Workout child class
    def generate_workout():
        #clear()
        workout_group = int(input('What kind of workout would you like to do? Please select a number: \n 1: HIIT\n 2: Core\n 3: Strength '))
        if workout_group not in range(1,4):
            print('Invalid entry. Please enter corresponding number from menu.') #Error Handling
            HealthAssistant.generate_workout()
            return
        else:
            pass
        length_choice = int(input('How would you like to measure your workout? Please select a number: \n 1: Time \n 2: Repetitions: ')) 
        if length_choice not in range(1,3): 
            print('Invalid entry. Please enter corresponding number from menu.')#Error Handling
            HealthAssistant.generate_workout()
            return
        else:
            pass
        length_type = []
        if length_choice == 1:
            length_type.append('Time')
        else:
            length_type.append('Reps') 
        length = int(input('Enter length of workout'))
        #if type(length) != 'int':
        #    print('Invalid entry. Please enter corresponding number from menu.')
        #    HealthAssistant.generate_workout()
        #else:
        #    pass
        if workout_group == 1:
            HIIT(length_type[0], length).create_workout()
        elif workout_group == 2:
            Core(length_type[0], length).create_workout()
        elif workout_group == 3:
            Strength(length_type[0], length).create_workout()
        
        HealthAssistant.finish()
        return
    
    #This method allows user to input new exercises to excises of the Workout child classes
    def add_to_catolog():
        clear()
        exercise_add = input('What exercise would you like to add?: ')
        workout_group = int(input('What kind of workout is new exercise? Please select a number: \n 1: HIIT\n 2: Core\n 3: Strength '))
        if workout_group == 1:
            HIIT.add_workout(cls=HIIT, exercise = exercise_add)
        elif workout_group == 2:
            Core.add_workout(exercise_add)
        elif workout_group == 3:
            Strength.exercises.append(exercise_add)
        else:
            print('Invalid entry. Please enter corresponding number from menu.')
            HealthAssistant.add_to_catolog()    
        
        HealthAssistant.finish()
        return
   
    #This class method takes user input to create/log instance of meal class
    def log_a_meal():
        #clear()
        food_item = input('What did you eat?: ')
        try:
            cals = int(input('How many calories was this item: '))
        except:
            print('Invalid entry. Please enter calories as a whole number')
            HealthAssistant.log_a_meal()
            return
        comm = input('Any comments on the entry? Press enter to skip.')
        Meal(food_item, cals, comment=comm)
        print('Entry successful!')
        HealthAssistant.finish()
        return
    
    #This method returns a print out of the logs in the Workout and Meal classes
    def view_log():
        clear()
        print("\nHere's a look at your health activity: ")
        print(' Workouts:')
        for key, value in Workout.workout_log.items():
            print(' {}:'.format(key))
            for i in value:
                print('   '+i)
        print(' Meals:')
        for key, value in Meal.food_log.items():
            total_cals = 0
            print('  {}:'.format(key))
            for i in value:
                total_cals += value[value.index(i)][1]
                if len(value)==2:
                    print('   {}.{} - {} calories '.format(value.index(i)+1,value[value.index(i)][0],value[value.index(i)][1]))
                else:
                    print('   {}.{} - {} calories - {} '.format(value.index(i)+1,value[value.index(i)][0],value[value.index(i)][1],value[0][2])) 
            print('  On {}, you consumed a total of {} calories.'.format(key,total_cals))
        HealthAssistant.finish()
        return                            
    
    #This method is to prompt users to select functionality of the program they want to use    
    @classmethod
    def get_action(cls): 
        action = strftime("%Y-%m-%d %H:%M:%S", gmtime()) #Creating a unique timestamp id for every self.action
        HealthAssistant.all_actions.append(action)
        return (int(input('What would you like to do? Please select a number: \n 1: Generate workout\n 2: Add to workout catalog\n 3: Log a meal \n 4: View activity log '))) 
    
    #This method uses the get_action method(right above)to take users menu choice and calls the corresponding class method
    def perform(): 
        clear()
        if len(HealthAssistant.all_actions) <1:
            print("Hello! Welcome to your health assistant!\nThis asssistant can create your workouts, track your workouts and meals, count calories. \nIf you want to create a workout select option 1 from the main menu, to add a new exercise to a workout group, select option 2. If you'd like to log a meal, select option 3. To view all of your activity select option 4.\n")

            
        action = HealthAssistant.get_action()
        if action not in range(1,5):
            print('Invalid entry. Please enter corresponding number from menu.') #Error checking to ensure valid entry
            HealthAssistant.perform()
        else:
            pass
        if action == 1:
            clear()
            HealthAssistant.generate_workout()
        elif action ==2:
            clear()
            HealthAssistant.add_to_catolog()
        elif action == 3:
            clear()
            HealthAssistant.log_a_meal()
        elif action == 4:
            clear()
            HealthAssistant.view_log()
        return   
#End of HealthAssistantClass

    
#The code below runs the program for the user to interact with from the command line
HealthAssistant.perform()
