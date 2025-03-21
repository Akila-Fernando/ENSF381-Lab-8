import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

# print(soup.prettify())

acount = 0
atags = soup.find_all('a')
for i in atags:
    acount += 1
print(acount)

pcount = 0
ptags = soup.find_all('p')
for i in ptags:
    pcount += 1
print(pcount)

headers=["h1","h2","h3","h4","h5","h6"]

hcount = 0
for x in headers:
    htags = soup.find_all(x)
    for i in htags:
        hcount += 1
print(hcount)


words = soup.get_text().split()

wordcounts = {}

for word in words:
    if (word.lower()) in wordcounts:
        wordcounts[word.lower()] += 1
    else: 
        wordcounts[word.lower()] = 1


frequentwords = []
for i in range(5):
    maxword = None
    maxcount = 0

    for word in wordcounts:
        if maxword is None or wordcounts[word] > maxcount:
            maxword = word
            maxcount = wordcounts[word]

    if maxword:
        frequentwords.append((maxword, maxcount))
        del wordcounts[maxword]


for word, count in frequentwords:
    print(f"{word}: {count}")