
"""Exercise 5: This program records the domain name (instead of the address) 
where the message was sent from instead of who the mail came from (i.e., the 
whole email address). At the end of the program, print out the contents of 
your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}"""

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
    if len(words) != 0 and words[0] == 'Received:' : 
        print(words[2])
#         masterFile[words[1]] = masterFile.get(words[1],0) + 1
# print('Counts', masterFile)