import pandas as pd

dataset = pd.read_csv('googleplaystore_user_reviews.csv')
dataset.head(10)
dataset = dataset[:5000]
#dataset['App'].value_counts()

dataset['Sentiment'].value_counts()
dataset = dataset.dropna()
review = dataset['Translated_Review']
label = dataset['Sentiment']
positive_df = dataset[(dataset['Sentiment'] == 'Positive')]
negative_df = dataset[(dataset['Sentiment']=='Negative')]
neutral_df = dataset[(dataset['Sentiment']=='Neutral')]




#step-1 to join all the positive reviews together
#step-2 to split step-1 into words and covert in smaller letter
#step-3 to sort the top 30 frequently used words 


def word_to_freq(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

def sort_frequency(freqdict):
    sorte = [(freqdict[key], key) for key in freqdict]
    sorte.sort()
    sorte.reverse()
    return sorte

def get_top_n_words(list_of_reviews,n):
  all_words = "\n".join(list_of_reviews)
  all_words = all_words.lower().split()
  return sort_frequency(word_to_freq(all_words))[:n]
  
positive_list = get_top_n_words(positive_df["Translated_Review"][:],15)
pos_words = []
for poswords in positive_list:
    pos_words.append(poswords[1])

negative_list = get_top_n_words(negative_df["Translated_Review"][:],15)
neg_words = []
for negwords in negative_list:
    neg_words.append(negwords[1])
    
neutral_list = get_top_n_words(neutral_df["Translated_Review"][:],20)
neu_words = []
for neuwords in neutral_list:
    neu_words.append(neuwords[1])
#test_pos = ['awesome', 'worth', 'thanks', 'amazing', 'simple', 'perfect', 'price', 'everything', 'ever', 'must', 'ipod', 'before', 'found', 'store', 'never', 'recommend', 'done', 'take', 'always', 'touch']
#test_neg = ['waste', 'money', 'crashes', 'tried', 'useless', 'nothing', 'paid', 'open', 'deleted', 'downloaded', 'didn’t', 'says', 'stupid', 'anything', 'actually', 'account', 'bought', 'apple', 'already']
#test_neu = ['ok']
df = dataset[:]
for i in df.index.tolist():
    for word in df.at[i, "Translated_Review"].lower().split():
        if word in pos_words:
            df.at[i, word] = 1
        elif word in neg_words:
            df.at[i, word] = -1
        elif word in neu_words:
            df.at[i, word] = 0

df = df.d
    
    #Train Accuracy
    train_acc = accuracy_score(y_train, pred_train, normalizerop(["App", "Translated_Review", "Sentiment_Polarity", "Sentiment_Subjectivity"], axis =1)
#df.tail()

x = df.drop(["Sentiment"], axis =1)
x = x.fillna(0)
y = dataset.drop(["App", "Translated_Review", "Sentiment_Polarity", "Sentiment_Subjectivity"], axis =1)[:]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25, random_state =0)

from sklearn.metrics import accuracy_score,confusion_matrix
def train_test_accuracy(Classifier,X_train,y_train,X_test,y_test):
    
   #Train Model Fitting
    Classifier.fit(X_train,y_train)
    '''pred_train = Classifier.predict(X_train)
    print(pred_train)=True) * float(100)
    '''
        
    pred_test = Classifier.predict(X_test)
    test_acc = accuracy_score(y_test, pred_test, normalize=True) * float(100)
    
    #Printing train and test accuracy
    print('\nTrain accuracy = %f%%' % (train_acc))
    print('\nTest accuracy =  %f%%' % (test_acc))

from sklearn.linear_model import LogisticRegression
classifier1 = LogisticRegression(C =0.1, solver='newton-cg',multi_class='ovr')
train_test_accuracy(classifier1,x_train,y_train,x_test,y_test)