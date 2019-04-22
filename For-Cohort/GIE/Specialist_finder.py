#importing libraries
import pandas as pd

#importing dataset
dataset = pd.read_csv('ProtoSem19.1_Operations - GIE_Rubric.csv')

#function to get mostly common tech word
def get_buzz_word(list_of_aoi,n):
    all_words = '\n'.join(list_of_aoi)
    all_words = all_words.replace('/',' ').replace('[',' ').replace(']',' ').replace(',',' ').lower().split()
    return word_sort(word_count(all_words))[:8]

#function to count the frquency of words
def word_count(word_list):
    word_freq = [word_list.count(p) for p in word_list]
    return dict(zip(word_list, word_freq))

#fucntion to sort the top n words  
def word_sort(freq_dict):
    sorte = [(freq_dict[key], key) for key in freq_dict]
    sorte.sort(reverse = True )
    return sorte

#visalizing buzz words    
buzz_word_tuple = get_buzz_word(dataset["Areas of Interest (The Developer Groups within ProtoSem)"],5)
buzz_word =[]
for word in buzz_word_tuple:
    print("\nWord {}{}{} is used {}{}{} times.".format("'",word[1].capitalize(),"'","'", word[0],"'"))
    buzz_word.append(word[1])

#flags
flag =0 
fun_flag =0

#input for finding specialist
while(flag !=1):
    search = str(input("\nEnter one of the Buzz-Words :"))
    if search not in buzz_word:
        print("\n         ! Please enter one of the buzz word !")
        for count,j in enumerate(buzz_word):
            print("\n{}. {}".format(count, j))
            flag =0
            fun_flag =1
    else:
        flag = 1

#collects the Name and email of specialists
namelist =[]
emaillist = []
print("\nThe following people may help you out with {} :)".format(search))
for i, list_item in enumerate(dataset['Areas of Interest (The Developer Groups within ProtoSem)']):
    if search in list_item.replace('/',' ').replace('[',' ').replace(']',' ').replace(',',' ').lower().split():
        namelist.append(dataset.at[i, "Name"])
        emaillist.append(dataset.at[i, "Email Address"])

#returns the name of the specialists
for g,name in enumerate(namelist):
    print("\n{}. {}".format(g+1, name.capitalize()))

#input for wanting mail ID or Not:
question1 = str(input("\nDo you want email id for these persons?\n\nEnter Yes or No >> ")).lower()

#returns mail ID of particular person
if question1 == 'yes':
    for h,mail in enumerate(emaillist):
        print("\n{}. {}".format(h+1,mail))
    question2 = input("\nDo you want particular's email id?\n\nEnter Yes or No >> ")
    if question2 == 'yes':
        who = input("\nWhose E-mail ID?\n\nEnter First-name >> ")
        for mail1 in emaillist:
            firstname = mail1.split('.')
            if firstname[0] == who:
                print("\nEmail ID >> ", mail1)
                print("\nHave a nice day | Happy to help :)\n")
    else:
        print("\nHave a nice day | Happy to help :)\n")
#The END
else:
    print("\nHave a nice day | Happy to help :)\n")

#just for fun
if fun_flag == 1:
    print("Sodhikkadhinga da ennaya ):")
