
##DONE

"""Exercise 2: Write a program that categorizes each mail message by 
which day of the week the commit was done. To do this:

- look for lines that start with "From", 
- then look for the third word 
- keep a running count of each of the days of the week.
- at the end of the program print out the contents of your dictionary (order does not matter).

Sample Line:

    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Sample Execution:

python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}"""

#fileName = input('Please enter your file name: ')
fileName = 'mbox-short.txt'
masterFile = dict()

try: 
    fhand = open(fileName)
except: 
    print('Your file could not be opened:', fileName)
    exit()

for line in fhand: 
    words = line.split()
    #print(words)
    if len(words) != 0 and words[0] == 'From' : 
        #print(words[2])
        masterFile[words[2]] = masterFile.get(words[2],0) + 1
print('Counts', masterFile)
