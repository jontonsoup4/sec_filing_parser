from html2text import html2text
import requests
from bs4 import BeautifulSoup
import pprint
import os

url = input("What is the URL?\n")
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
folder = url.split('/')[-1].replace('.htm', '').replace('.html', '') + '/'    # naming folder by url
if not os.path.exists(folder):    # making a folder if not present
    os.makedirs(folder)
doc = open(folder + 'document.txt', 'w+', newline='\n')
doc.write(html2text(soup.prettify()).replace('-', '').replace('|', '')
          .replace('¨', '☐').replace('ý', '☑'))
cashmoney = []    # making a list to add the $ paragraphs to
doc.seek(0)
fulltext = doc.read()    # opening the document
paragraphs = fulltext.split('\n\n')    # splitting the document into paragraphs
for paragraph in paragraphs:
    if len(paragraph) > 70 and '$' in paragraph:
            cashmoney.append({'text': paragraph[:70].replace('\n', ' ') + '...', 'start': fulltext.index(paragraph),
                              'stop': fulltext.rindex(paragraph[-70:]) + 70})    # indexing paragraphs
paraprint = open(folder + 'paragraph.txt', 'w')
pprint.pprint(cashmoney, width=100, stream=paraprint)    # making it look pretty
print("Done!")    # it worked
