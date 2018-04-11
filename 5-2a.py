"""5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 

Once 'done' is entered, print out the largest and smallest of the numbers. 

If the user enters anything other than a valid number catch it with a try/except and put out an 
appropriate message and ignore the number. 

Enter 7, 2, bob, 10, and 4 and match the output below."""

maximum = None
minimum = None

while True : 
    userEntered = input("Please enter a integer: ")
    # testMax = userEntered
    # testMin = userEntered
    
    if userEntered == 'done' :
        break
    try:
        if maximum is None or float(userEntered) > maximum : 
            maximum = float(userEntered)
        elif minimum is None or float(userEntered) < minimum : 
            minimum = float(userEntered)
    except:
        print("invalid input")
print('Largest:', int(maximum), ' Smallest: ', int(minimum))
    