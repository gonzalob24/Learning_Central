
# Whats needed prior to web scraping

# 1.) BeautifulSoup, which you can download by typing: pip install beautifulsoup4 or conda install beautifulsoup4 (for the Anaconda distrbution of Python) in your command prompt.

# 2.) lxml , which you can download by typing: pip install lxml or conda install lxml (for the Anaconda distrbution of Python) in your command prompt.

# 3.) requests, which you can download by typing: pip install requests or conda install requests (for the Anaconda distrbution of Python) in your command prompt.



# Some things you should consider before web scraping a website:
# 1.) You should check a site's terms and conditions before you scrape them.

# 2.) Space out your requests so you don't overload the site's server, doing this could get you blocked.

# 3.) Scrapers break after time - web pages change their layout all the time, you'll more than likely have to rewrite your code.

# 4.) Web pages are usually inconsistent, more than likely you'll have to clean up the data after scraping it.

# 5.) Every web page and situation is different, you'll have to spend time configuring your scraper.

import requests
import pandas as pd

from bs4 import BeautifulSoup
from pandas import Series, DataFrame

url = 'http://www.ucop.edu/operating-budget/budgets-and-reports/legislative-reports/2013-14-legislative-session.html'


# Now let's go ahead and set up requests to grab content form the url, 
# and set it as a Beautiful Soup object.

result = requests.get(url)

content = result.content

# Set as Beautiful Soup Object
soup = BeautifulSoup(content)

# Go to the section of interest in the website
summary = soup.find('div', {'class':'list-land', 'id':'content'})

# Find the tables in the HTML site
tables = summary.find_all('table')


# Now we need to use Beautiful Soup to find the table entries. 
# A 'td' tag defines a standard cell in an HTML table. 
# The 'tr' tag defines a row in an HTML table.

# We will parse through our tables object and try to find each cell using the 
# findALL('td') method.

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all

# empty data list
data = []

# Set rows as first indexed object in tables with a row
rows = tables[0].findAll('tr')

# now grab every HTML cell in every row

for tr in rows:
    cols = tr.findAll('td')
    # Check to see if text is in the row
    for td in cols:
        text = td.find(text=True) 
        print (text)
        data.append(text)


# Now we'll use a for loop to go through the list and grab only the cells 
# with a pdf file in them, we'll also need to keep track of the index to 
# set up the date of the report.

# Set up Dates and Reports as Series
reports = []
date = []

index = 0
num = 1
for item in data:
    if 'pdf' in item:
        date.append(data[index - 1])
        reports.append(item.replace(u'\xa0', u' '))
    index += 1

# You'll notice a line to take care of '\xa0 ' This is due to a unicode 
# error that occurs if you don't do this. Web pages can be messy and 
# inconsistent and it is very likely you'll have to do some research to 
# take care of problems like these.
# https://stackoverflow.com/questions/10993612/python-removing-xa0-from-string

date = Series(data)
reports = Series(reports)

legislative_df = pd.concat([date, reports], axis = 1)
legislative_df.columns = ['Date', 'Report']

print(legislative_df)


