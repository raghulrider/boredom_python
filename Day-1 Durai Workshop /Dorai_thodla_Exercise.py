#importing libraries
import pandas as pd
from bs4 import BeautifulSoup

#using beautiful soup to read html document
html = open("Database - Wikipedia.html").read()
soup = BeautifulSoup(html)

#counts the letters
letters = dict()
for i,letter in enumerate(soup.get_text()):
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