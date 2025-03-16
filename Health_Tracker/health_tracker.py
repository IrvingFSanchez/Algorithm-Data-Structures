#Name: Irving F. Sanchez
#Course: Algorithm and Data Structures SP25-CPSC-34000-002
#School: Lewis University, Romeoville, IL
#Purpose: Design a python program that tracks daily health-related data

'''Note: I put a ton of comments in my code for personal use, I add notes to help me understand what
I'm doing and why I'm doing it.I'm not sure if this is a good practice or not, but I'm doing it for now.'''


''' /*---+---+---+--Start of Variable Trackers Block---+---+---+--*/ '''
# We need a way of tracking variables so we initialize them with a beginning value
water_total = 0 # We want to track total water intake measured in ounces
activity_total = 0 # We want to track total activity measured in minutes
ai_tracker = -1 
''' /*---+---+---+--End of Variable Trackers Block---+---+---+--*/ '''


''' /*---+---+---+--Start of Constant Definitions Block---+---+---+--*/ '''
WATER_GOAL = 64 # The goal is to drink 64 ounces of water a day
ACTIVITY_GOAL = 30 # The goal is to be active for 30 minutes a day
''' /*---+---+---+--End of Constant Definitions Block---+---+---+--*/ '''


''' /*---+---+---+--Start of Water Intake Function Block---+---+---+--*/ '''
# Here we are going to log the water intake
def water_intake_log(): 
    global water_total
    while True:
        try:
            # We need to ask the user to input the amount of water they have consumed
            water = float(input("Please enter the amount of water you have consumed in ounces: "))
            if water < 0:
                # We need to ensure that the water intake they input is not a negative number
                print("Please enter a positive number (ノಠ.ಠ)/ ")
            else:
                # We then need to take the input and add it to the water total variable we set earlier in the variable tracker section
                water_total += water
                print(f"Your total water intake is now {water_total} ounces!")
                break # Once they input the water intake we can exit the loop after successfully adding the water intake to the total
        except ValueError:
            # It's always good practice to take care of any invalid input the user may input
            print("Please enter a valid number (ノಠ.ಠ)/ ")
''' /*---+---+---+--End of Water Intake Function Block---+---+---+--*/ '''


''' /*---+---+---+--Activity Intake Function Block---+---+---+--*/ '''
# Here we are going to log the activity intake
def activity_log():
    global activity_total
    while True:
        try:
            # We need to ask the user to input the amount of activity they have done in minutes
            activity = float(input("Please enter the amount of activity you have done in minutes: "))
            if activity < 0:
                # Like previous we need to ensure we can oppose any negative numbers user may input
                print("Please enter a positive number (ノಠ.ಠ)/ ")
            else:
                # Provided we were given a positive number or a non-negative number we can add the input to the activity total variable
                activity_total += activity
                print("Activity has been logged successfully! ᕙ(ಠ.ಠ)ᕗ")
                break
        except ValueError:
            print("Please enter a valid number (ノಠ.ಠ)/")
''' /*---+---+---+--End of Activity Intake Function Block---+---+---+--*/ '''

            
''' /*---+---+---+--Start of Remaining Goal Function Block---+---+---+--*/ '''
# Here we want to calculate the remaining goal for water and activity
def daily_totals():
    remain_water = max(WATER_GOAL - water_total, 0) # We want to calculate the remaining water goal
    remain_activity = max(ACTIVITY_GOAL - activity_total, 0) # We want to calculate the remaining activity goal
    
    # Here we are going to display the daily total
    print("\nDaily Totals:")
    print(f"- Water Consumed: {water_total} oz (Goal: {WATER_GOAL} oz, Remaining: {remain_water} oz)")
    print(f"- Activity: {activity_total} min (Goal: {ACTIVITY_GOAL} min, Remaining: {remain_activity} min)")
    
    # Here we are going to give a little bit of encouragement and provide a message based on the user's progress
    if water_total >= WATER_GOAL and activity_total >= ACTIVITY_GOAL:
        print("Congratulations! You have met both your water intake and activity goals for the day! ᕙ( ͡❛ ʖ ͡❛)ᕗ ")
    elif water_total >= WATER_GOAL:
        print("Great job! You've met your water intake goal for the day!ᕙ( ͡❛ ᴗ ͡❛)ᕗ ")
    elif activity_total >= ACTIVITY_GOAL:
        print("Great job! You've met your activity goal for the day!ᕙ( ͡❛ ₒ ͡❛)ᕗ ")
''' /*---+---+---+--End of Remaining Goal Function Block---+---+---+--*/ '''


''' /*---+---+---+--Start of Data Reset Block---+---+---+--*/ '''
# This will be the function to reset all tracked data to zero
def reset_data():
    global water_total, activity_total # We need to access the global variables to reset them
    water_total = 0
    activity_total = 0
    print("Data has been reset successfully! (ノಠ.ಠ)/ ┻━┻ ")
''' /*---+---+---+--End of Data Reset Block---+---+---+--*/ '''


''' /*---+---+---+--Start of Menu Display Block---+---+---+--*/ '''
def menu_display():
    print("1. Log Water Intake")
    print("2. Log Activity Time")
    print("3. View Daily Totals")
    print("4. Reset Data")
    print("5. Exit")
''' /*---+---+---+--End of Menu Display Block---+---+---+--*/ '''


''' /*---+---+---+--Start of Main Function Block---+---+---+--*/ '''
# This is the main function that will run the program
def main():
    while True:
        menu_display()
        choice = input("Please enter your choice: ")
        
        # Here we are going to check the user's input and call the appropriate function
        if choice == '1':
            water_intake_log()
        elif choice == '2':
            activity_log()
        elif choice == '3':
            daily_totals()
        elif choice == '4':
            reset_data()
        elif choice == '5':
            print("Exiting program...Peace Out ┏( ͡ㆆ ʖ ͡ㆆ)┛")
            break
        else:
            # To handle invaluid user choices
            print("Invalid choice. Please try again. (ノಠ.ಠ)/ ┻━┻")
''' /*---+---+---+--End of Main Function Block---+---+---+--*/ '''


''' /*---+---+---+--Start of Program Execution Block---+---+---+--*/ '''
# Here we run the program
if __name__ == "__main__":
    main()
''' /*---+---+---+--End of Program Execution Block---+---+---+--*/ '''