#importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
df = pd.read_csv('protosem_attendance.csv', header =None)

#data preprocessing :)
dataset = df[:5]
dataset = dataset.drop(columns = [0,1,62,63,64,65,66,67], axis =1)
dataset = dataset.T
dataset = dataset.drop([0,1], axis = 1)

dataset[4].value_counts()

x = dataset.iloc[:, [2]].values
y = dataset.iloc[:, [0]]
y = y.convert_objects(convert_numeric = True)
y.infer_objects()
y.info()
# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
x[:, 0] = labelencoder_X.fit_transform(x[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
x = onehotencoder.fit_transform(x).toarray()

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 0)

y_train = y_train.fillna(0)
# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)
type(y_train[2])
# Visualising the Training set results
plt.scatter(X_train,y_train ,color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.show()

len(X_train)
len(y_train) 
a = [1,0,0,1,0,1,0,1]
b = [1,2,3,4,5,3,2,4]
# Visualising the Test set results
plt.scatter(a, b, color = 'red')
#plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.show()