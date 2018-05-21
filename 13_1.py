"""Exercise 1: Change the socket program socket1.py to:

- Prompt the user for the URL so it can read any web page. 
 
- Use split('/') to break the URL into its component parts so you can extract the host 
 name for the socket connect call. 
 
- Use try and except to handle the condition where the user enters an improperly 
 formatted or non-existent URL."""

import socket
askurl = input('please enter a web url as an example: http://data.pr4e.org/romeo.txt \n')
# print(askurl)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
spliturl = askurl.split('/')
# print(spliturl)
domain = spliturl[2]
# print(domain)
mysock.connect((domain, 80))
# cmd = 'GET' askurl 'HTTP/1.0\r\n\r\n'.encode()
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
print(cmd)
# mysock.send(cmd)


# while True:
#     data = mysock.recv(20)
#     if (len(data) < 1):
#         break
#     print(data.decode(),end='')

# mysock.close()