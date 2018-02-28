# Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
# Formula to convert from C to F Multiply the °C temperature by 1.8. Add 32 to this number. This the answer in °F.

#accept user input in the form of a int or float
tempC = input('Please enter a temperature in Celsius \n')

#convert the inputed number into a float and assign to ftempC
ftempC = float(tempC)

# perform the conversion and assign it to tempF
tempF = (ftempC * 9/5) + 32

# convert the float to a string assign to converted
converted = str(tempF)

# print out the converted number
#print(converted)
print("Temperature:", ftempC, "Celsius =", converted, "F")
