# rating: the average rating on a 1-5 scale achieved by the book
# review_count: the number of Goodreads users who reviewed this book
# isbn: the ISBN code for the book
# booktype: an internal Goodreads identifier for the book
# author_url: the Goodreads (relative) URL for the author of the book
# year: the year the book was published
# genre_urls: a string with '|' separated relative URLS of Goodreads genre pages
# dir: a directory identifier internal to the scraping code
# rating_count: the number of ratings for this book (this is different from the number of reviews)
# name: the name of the book

import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
#import seaborn as sns


#Write a function that accepts an author url and returns the author's name based on your experimentation above
def get_author(url):
    #######
    #   Insert your code
    name = url.split('.')[-1]
    #######
    return name



#Write a function that accepts a genre url and returns the genre name based on your experimentation above
def split_and_join_genres(url):
    #######
    #   Insert your code
    gener = url.split('|')
    #######
    return gener

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)

#Read the data into a dataframe
df = pd.read_csv("data/goodreads.csv")

#Examine the first couple of rows of the dataframe
#######
#   Insert your code
#print(df.head())
#######

df=pd.read_csv("data/goodreads.csv", header=None,
               names=["rating", 'review_count', 'isbn', 'booktype',
                      'author_url', 'year', 'genre_urls', 'dir','rating_count', 'name'])

#Examine the first couple of rows of the dataframe
#######
#   Insert your code
#print(df.head())

#######

#Start by check the column data types
#######
#   Insert your code
#print (df.dtypes)
#######

#Come up with a few other important properties of the dataframe to check
#######
#   Insert your code
#First let's drop missing values and nan
cleanedDf = df.dropna(axis = 0, how ='any')

#We might need to convert some columns datatypes
cleanedDf['review_count'] = cleanedDf['review_count'].astype(int)
#print(cleanedDf.dtypes)
#print (cleanedDf.head())
#######

#Get a sense of how many missing values there are in the dataframe.
#######
#   Insert your code
missingValues   =   df.isnull().sum()
#print(missingValues)
#######

#Treat the missing or invalid values in your dataframe
#######
#   Insert your code
#We can replace the nan values with some static values
df = df.replace(np.nan,'not-found')
#######


#Check the column data types again
#######
#   Insert your code
#print(df.dtypes)
#######

#Convert rating_count, review_count and year to int
#######
# .Insert your code
cleanedDf['rating_count'] = cleanedDf['rating_count'].astype(float)
cleanedDf['review_count'] = cleanedDf['review_count'].astype(int)
cleanedDf['year'] = cleanedDf['year'].astype(int)

cleanedDf.loc[cleanedDf.genre_urls.isnull(), 'genre_urls']=""
cleanedDf.loc[cleanedDf.isbn.isnull(), 'isbn']=""
#print(cleanedDf.dtypes)

#######

#Part 3: We will need author and genre to proceed! Parse the author column from the author_url and genres column from the genre_urls. Keep the genres column as a string separated by '|'.

cleanedDf['author'] =   cleanedDf['author_url'].map(get_author)
cleanedDf['genres'] =   cleanedDf['genre_urls'].map(split_and_join_genres)
print(cleanedDf.head())
