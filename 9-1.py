"""Write a program that reads the words in words.txt and stores 
them as keys in a dictionary. It doesn't matter what the values 
are. Then you can use the in operator as a fast way to check 
whether a string is in the dictionary."""

#fileName = input('Please enter your file name: ')
fileName = 'romeo.txt'
masterFile = dict()

try: 
    fhand = open(fileName)
except: 
    print('Your file could not be opened:', fileName)
    exit()

for lines in fhand: 
    #print(lines)
    #strip out the spaces and new line in the file
    line = lines.strip()
    #print(line)
    #split up the words in a list
    words = line.split()
    #print(words)
    #grab each word to perform the check
    for word in words:
        #print(word)
        if word not in masterFile: 
            masterFile[word] = 1
        else: #this makes a histogram and adds 1 if the word is in the dictionary already.
            masterFile[word] = masterFile[word] + 1
        #or remove the if else statement above, and use this:
        #masterFile[word] = masterFile.get(word,0) + 1
        
print(masterFile)
