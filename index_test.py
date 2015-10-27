url = input("What is the URL?\n")
folder = url.split('/')[-1].replace('.htm', '').replace('.html', '') + '/'    # naming folder by url
doc = open(folder + 'document.txt', 'r', newline='\n')
fulltext = doc.read()
start = int(input('Index Start Value:\n'))
stop = int(input('Index Stop Value:\n'))
print('\n')
print(fulltext[start:stop])