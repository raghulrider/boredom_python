#importing libraries
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

#fetching text from url
with urllib.request.urlopen("https://en.wikipedia.org/wiki/Database") as url:
    html = url.read()
soup = BeautifulSoup(html)
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text().lower()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)

#getting word out of text and creating dataframe
words = text.split()
words_df = pd.DataFrame(words, columns = ['Words'])

#fix to eliminate  ',' and '.' that interrupts counting
def fix_value(word_str):
    word_str = word_str.replace(',','')
    word_str = word_str.replace('.','')
    word_str = word_str.replace('databases','database')
    return(word_str)

#calling fix function    
words_df["Words"] = words_df["Words"].apply(fix_value)

#counting words
word_count = dict()
for i in words_df["Words"]:
    if i not in word_count:
        word_count[i] = 1
    else:
        word_count[i] = word_count[i] + 1

#segregating top 10 frequently used words
word_count_swapped = dict([(value, key) for key, value in word_count.items()]) 
frequent_words =[]
for key,value in word_count_swapped.items():
    if key>97:
        frequent_words.append([value,key])
        frequent_words.sort()
print(frequent_words)
#creating dataframe for most frequently used words
frequent_words_df = pd.DataFrame(frequent_words, columns = ['Word', 'Count'])

#visualizing the frequently used letters
frequent_words_df.set_index("Word", drop = True, inplace = True)
frequent_words_df.plot()
frequent_words_df.plot.bar() 