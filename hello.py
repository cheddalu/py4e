
"""5.2 Write a program that repeatedly prompts a user for 
integer numbers until the user enters 'done'. Once 'done' 
is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it 
with a try/except and put out an appropriate message and ignore 
the number. Enter 7, 2, bob, 10, and 4 and match the output below."""

#prompt user for integer until 'done' is indicated
user_input = 0

#print largest and smallest number
large = 0
small = 0

while True: 
    user_input = input('Please enter in a integer: ')
    try:
        if user_input == 'done':
            break
    except ValueError: 
        break
    #print('You entered', user_input)
    else : 
        if int(user_input) > int(large) and int(user_input) < int(small) :
            large = int(user_input)
            print('large: ', large)
            #if int(user_input) < int(small) : 
            small = int(user_input)
            print('small ', small)
    
#user try/except to catch anything other than integers entered. 


