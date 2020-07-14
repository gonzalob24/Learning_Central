import socket
import urllib.request
from bs4 import BeautifulSoup

# Simple  web browser
# mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysocket.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # encode prepares to send, encode to UTF-8
# mysocket.send(cmd)

# while True:
#     data = mysocket.recv(512) # received bytes
#     if (len(data) < 1):
#         break
#     print(data.decode()) # decode bytes to get UTF-8

# mysocket.close()

# text processing 

# characterset websites use UTF-8 1-4 bytes per character. Has a dinamic length
# Python 3.0 unicode and str are the same. Internally all str are UNICODE. 
# In Python two type unicode and str are different

# print(ord('a'))

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())


# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
# for line in fhand:
#     print(line.decode().strip())


# HTML Parsing
# url = 'http://www.dr-chuck.com/page1.html'
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html-parser') # parse the data

# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

### XML #### Extensible Markup Language
# Can name tags with any name
# Serialize / De-Serialize
# Has Nodes

## XML Schema
# XSD -> W#C Schema specification for XML
# xs:element. xs:sequence xs:complexType

class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 2
        print(self.x)


an = PartyAnimal()
print(dir(an))
