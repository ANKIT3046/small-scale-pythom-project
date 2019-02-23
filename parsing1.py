import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


#ignore SSL certificate errors

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode =ssl.CERT_NONE


url = input('Enter URL to scrap: ')
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)

tag_list = list()
# Repeats this count number of times
for i in range(count):
    print ("Retrieving:", url)
    # 3. Read HTML with urllib's urlopen() method
    html = urlopen(url, context=ctx).read()
    # 4. Parse HTML with BeautifulSoup's BeautifulSoup() method

    soup=BeautifulSoup(html,'html.parser')
    # 5. Retrieve list of anchor a tags
    tags = soup('a')

    # 6. Loop through to append tags to a list tag_list
    for tag in tags:
        tag_list.append(tag)

    # 7. Get new url based on (position - 1) due to nature of counts request
    url = tag_list[position - 1].get('href', None)
    print (tag_list)

    # 8. Delete the whole list for a new iteration through (3) to (7)
    del tag_list[:]

print ("Retrieving", url)
