"""Exercise 4: Add code to the above program to figure out who has the most 
messages in the file.

After all the data has been read and the dictionary has been created, look 
through the dictionary using a maximum loop (see Section [maximumloop]) to 
find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195"""

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
    # print(words)
    if len(words) != 0 and words[0] == 'From' : 
        # print(words[1])
        masterFile[words[1]] = masterFile.get(words[1],0) + 1
# print('Counts', masterFile)

largest = None 
for key in masterFile:
    # print(key)
    # print(masterFile[key])
    if largest is None or masterFile[key] > largest: 
        largest = masterFile[key]
        sender = key
print(sender, largest)