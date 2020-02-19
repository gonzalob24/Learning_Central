import socket

#open a socker 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) #I want to talk to port 80
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #enconde UTF8
mysock.send(cmd)

#retrieve data using a foor loop
while True:
    data = mysock.recv(512) #reveive up to 512 characters.
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
