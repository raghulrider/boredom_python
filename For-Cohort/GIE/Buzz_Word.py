#importing libraries
import pandas as pd

#importing dataset
df = pd.read_csv('ProtoSem19.1_Operations - GIE_Rubric.csv')

def get_buzz_word(list_of_aoi,n):
    all_words = '\n'.join(list_of_aoi)
    all_words = all_words.replace('/',' ').replace('[',' ').replace(']',' ').replace(',',' ').lower().split()
    return word_sort(word_count(all_words))[:n]

def word_count(word_list):
    word_freq = [word_list.count(p) for p in word_list]
    return dict(zip(word_list, word_freq))

def word_sort(freq_dict):
    sorte = [(freq_dict[key], key) for key in freq_dict]
    sorte.sort(reverse = True )
    return sorte    
buzz_word_tuple = get_buzz_word(df["Areas of Interest (The Developer Groups within ProtoSem)"],5)
buzz_word =[]
for word in buzz_word_tuple:
    print("Word {}{}{} is used {}{}{} times.".format("'",word[1].capitalize(),"'","'", word[0],"'"))
    buzz_word.append(word[1])
