import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

# print(soup.prettify())

#part 3: data analysis
links = 0
atags = soup.find_all('a')
for i in atags:
    links += 1
print(links)

paragraphs = 0
ptags = soup.find_all('p')
for i in ptags:
    paragraphs += 1
print(paragraphs)

headers=["h1","h2","h3","h4","h5","h6"]

headings = 0
for x in headers:
    htags = soup.find_all(x)
    for i in htags:
        headings += 1
print(headings)

#part 4: Keywords Analysis
userinput = input("Enter a keyword: ")
keyword = userinput.lower()
keywordcount = 0

words = soup.get_text().split()
for word in words:
    if word.lower() == keyword:
        keywordcount += 1

print(f"Keyword '{keyword}' appears {keywordcount} times")

#part 5: Word Frequency Analysis
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

# part 6: Finding the Longest Paragraph

parawordcounts = {}
maxwordcount = 0
longestparagraph = ""

for paragraph in ptags:
    words = paragraph.get_text().split()
    
    wordcount = len(words)

    if wordcount >= 5 and wordcount > maxwordcount:
        longestparagraph = paragraph.get_text()
        maxwordcount = wordcount

print(f"Longest Paragraph: {longestparagraph}, Number of words: {maxwordcount}")

# part 7: Visualizing Results

labels = ['Headings', 'Links', 'Paragraphs']
values = [headings, links, paragraphs]
plt.bar(labels, values)
plt.title('Group 9')
plt.ylabel('Count')
plt.show()