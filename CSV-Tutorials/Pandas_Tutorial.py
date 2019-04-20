#importing libraries
import pandas as pd

#importing dataset
df = pd.read_csv('googleplaystore.csv')  
print(df.head())

#data preprocessing (removing all NaN)
print('Length of Data Frame before:', len(df))
df = df.dropna()
print('Length of Dataframe after:', len(df))

df.describe()
df.info()

#covert object to numeric
df = df.convert_objects(convert_numeric = True)
df.describe()
df.info()

#segregating unique applications and calcualting average ratings
df["category"].unique()
for category in df["category"].unique():
    print(df[(df["category"] == category)]["rating"].mean())

#function to remove '+' and '' from Installs column 
def fix_install_col(install_str):
    install_str = install_str.replace('+','')
    install_str = install_str.replace(',','')
    return(install_str)
    
#Fixing Installs column and converting objects to numerics
df["Installs"] = df["Installs"].apply(fix_install_col)
df = df.convert_objects(convert_numeric = True)
df.describe()

#function remove 'M' and 'Varies with device' from Installs column 
def fix_size(size_str):
    size_str = size_str.replace('M','')
    size_str = size_str.replace('Varies with Device ','0')
    return(size_str)
    
#Fixing Size column and converting objects to numerics    
df["Size"] = df["Size"].apply(fix_size)
df = df.convert_objects(convert_numeric =True)
df.describe()

#Creating list and storing categories with ratings
ratings = []
for category in df["category"].unique():
    ratings.append([category, df[(df["category"] == category )]["rating"].mean()])
    
#converting list containing ratings to DataFrame     
ratings_df = pd.DataFrame(ratings, columns = ['Category', 'Ratings'])
print(ratings_df)

#Creating list and storing categories with ratings
reviews = []
for category in df["category"].unique():
    reviews.append([category, df[(df["category"] == category )]["Reviews"].mean()])
    
#converting list containing ratings to DataFrame     
reviews_df = pd.DataFrame(ratings, columns = ['Category', 'Reviews'])
print(reviews_df)

#Creating list and storing categories with ratings
installs = []
for category in df["category"].unique():
    ratings.append([category, df[(df["category"] == category )]["Installs"].mean()])
    
#converting list containing ratings to DataFrame     
installs_df = pd.DataFrame(ratings, columns = ['Category', 'Installs'])
print(installs_df)

#visualizing the ratings_df dataframe
ratings_df.set_index("Category", drop = True, inplace = True)
ratings_df.plot()
#ratings_df.plot.bar()      #for bar graph remove comment 

#visualizing the review_df dataframe
reviews_df.set_index("Category", drop = True, inplace = True)
reviews_df.plot()
#reviews_df.plot.bar()      #for bar graph remove comment 

#visualizing the installs_df dataframe
installs_df.set_index("Category", drop = True, inplace = True)
installs_df.plot()
#installs_df.plot.bar()    #for bar graph remove comment 