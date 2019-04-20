#import libraries
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

#fetching text from url
with urllib.request.urlopen("https://en.wikipedia.org/wiki/Database") as url:
    html = url.read()
soup = BeautifulSoup(html)
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = '\n'.join(chunk for chunk in chunks if chunk)

#counts the letters
letters = dict()
for i,letter in enumerate(text):
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] = letters[letter]+1

#swap keys and values
letters_swapped = dict([(value, key) for key, value in letters.items()]) 
print(len(letters_swapped))

#top ten frequently used letters
frequent_letters = []
for key,value in letters_swapped.items():
    if key>4000:
        frequent_letters.append([value,key])
#converting list to  dataframe        
frequent_letters_df = pd.DataFrame(frequent_letters, columns = ['Letter', 'Count'])

#visualizing the frequently used letters
frequent_letters_df.set_index("Letter", drop = True, inplace = True)
frequent_letters_df.plot()
frequent_letters_df.plot.bar() 