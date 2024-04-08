

#Question1
'''
read in all of the data from both of these files and store their info in dictionaries
open a new file called all_the_ages.txt
write all of the info from the dictionary to all_the_ages.txt
'''

age_dict = {} #lets start by making a dict for the ages

with open('ages.txt', 'r') as age_file: #open the .txt and assign it to age_file
    for line in age_file: #for each line in the file
        name, age = line.strip().split('/') #taje only the name and split them into seperate elements after each /
        age_dict[name] = age #assign the name as the key and the age as the value


with open('ages2.txt', 'r') as age_file: #open the .txt and assign it to age_file
    for line in age_file: #for each line in the file
        name, age = line.strip().split('/') #taje only the name and split them into seperate elements after each /
        age_dict[name] = age #assign the name as the key and the age as the value


with open('all_the_ages.txt', 'w') as all_the_ages: #open the .txt and assign it to all_the_ages
    for name, age in age_dict.items(): #for each name and age in the dict
        all_the_ages.write(f'{name}/{age}\n') #write  to the all_the_ages.txt file that we're operating in... the name and age to the file with a / between them and a new line at the end

print(age_dict) #print the dict to see if it worked





#Question2
'''
return the quotient of the two numbers
do type hints
use assert statements to not have a division by zero error
appropriate docstring
two test cases
'''

def find_the_quotient(num1:int, num2:int) -> float:
    '''
    This function will take 2 integers and return the quotient as a float, since most values will be a float when dividing

    Params: 
        num1(int) - the first number of the division equation
        num2(int) - the second number of the division equation

    returns: 
        quotient (float) - the returned value of the division problem

    >>> find_the_quotient(2/4)
    0.5
    
    >>> find_the_quotient(12/4)
    3.0
    '''

    assert num2 != 0, 'Cannot divide by zero' #assert that num2 is not 0 before going anywhere else with this division problem
    return num1/num2 #return the quotient of the two numbers

print(find_the_quotient(2,4)) #test case 1
print(find_the_quotient(12,4)) #test case 2



#Question3
'''
use the tkinter library to create a layout with a button and a label and entry box
'''

import tkinter as tk # traditional look

# Create the application window
window = tk.Tk()

find_label = tk.Label(window, text = 'Find what: ') #create a label that says 'Find what: '
replace_label = tk.Label(window, text= 'Replace with: ') #create a label that says 'Replace with: '

find_entry = tk.Entry(window) #create an entry box for the user to input text
replace_entry = tk.Entry(window) #create an entry box for the user to input text

find_button = tk.Button(window, text = 'Find Next') #create a button that says 'Find'
replace_button = tk.Button(window, text='Replace') #create a button that says 'Replace'

find_label.grid(row=0, column=0) #place the find_label in the window
replace_label.grid(row=1, column=0) #place the replace_label in the window

find_entry.grid(row=0, column=1) #place the find_entry in the window
replace_entry.grid(row=1, column=1) #place the replace_entry in the window

find_button.grid(row=0, column=2) #place the find_button in the window
replace_button.grid(row=1, column=2) #place the replace_button in the window

window.mainloop() #run the window


#Question4
'''
write an event handler func for calculating the area of a rectangle
when the calculate button is clicked the area should be displayed in the label
assume height, width, valculate and area_label is already made
'''

def calculate_area() -> None:
    '''
    This function will take the height and width from the user and calculate the area of the rectangle
    then display the area in the area_label, it's a button so we dont need any params or returns

    Params: 
        None

    returns: 
        None

    '''
    height * width #calculate the area of the rectangle


calculate['command'] = calculate_area #assign the calculate button to the calculate_area function
area_label['text'] = area #assign the area_label to the area of the rectangle



#Question5 
'''
write an event handler that handles many events at once
create a volume_calculator function that takes 1,5,10,100 depths

assume volume_1, volume_5, volume_10, volume_100, buttons are already made
'''
def volume_calculator(depth:int) -> Callable[[],None]:
    '''
    This function will be associated with buttons to calculate the total volume of a rectangle.
    It will take the height, width, and depth from the user and calculate the volume.

    Params:
        depth (int): The depth of the rectangle.
    
    Returns:
        None
    '''

    #im assuming these aren't made yet like in the previous question
    height = int(height_entry.get()) #get the height from the user
    width = int(width_entry.get()) #get the width from the user

    #the outer function will return a callable, which is the inner function, so we need the depth to be passed in the outer function
    def volume_calculate_inner(): #we have to make an inner function to return the volume
        volume = height * width * depth
        volume_label['text'] = volume #assuming the volume_label is already made, we will assign the text to the volume of the rectangle, similar to area label in Q4
        return volume_calculate_inner


# Assign the button commands to the volume_calculator function
volume_1['command'] = volume_calculator(1) #with the depth being passed in this outer function we will return the inner which is a proper callable
volume_5['command'] = volume_calculator(5)
volume_10['command'] = volume_calculator(10)
volume_100['command'] = volume_calculator(100)

    