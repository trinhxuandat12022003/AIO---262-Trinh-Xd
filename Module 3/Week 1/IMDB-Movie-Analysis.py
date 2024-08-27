import pandas as pd
dataset_path = r'C:\Users\Admin\Documents\AIO---262-Trinh-Xd\Module 3\Week 1\IMDB-Movie-Data.csv'

# Read data from .csv file
data = pd.read_csv(dataset_path)

# Read data with specified explicit index.
# We will use this later in our analysis
data_indexed = pd.read_csv(dataset_path, index_col="Title")

# Preview top 5 rows using head()
# print(data.head())
# Preview last 5 rows using tail()
# print(data.tail())
# print(data.info())
genre = data['Genre']
# print(genre)

columns = data[['Title', 'Genre', 'Actors', 'Director', 'Rating']]
# print(columns)

# print(data.set_index('Title'))

# print(data.set_index('Title').loc[['Suicide Squad']])

# print(data.iloc[10:15][['Title','Rating','Revenue (Millions)']])

# print(data['Revenue (Millions)'].quantile(0.95))

# print(data[((data['Year'] >= 2010) & (data['Year'] <= 2015))
#      & (data['Rating'] < 6.0)
#      & (data['Revenue (Millions)'] > data['Revenue (Millions)'].quantile(0.95))])

# print(data[['Director', 'Rating']])

# print(data.groupby('Director')[['Rating']].mean().head())

# x = data.groupby('Director')[['Rating']].mean()
# print(x.sort_values(['Rating'], ascending=False).head())

# To check null values row-wise
# print(data.isnull().sum())

# print(data[data.isnull().any(axis=1)])

# print(data.dropna().shape)

# print(data.dropna())

# print(data.fillna(300).shape)

# print(data.fillna(300))

# Use drop function to drop columns
# print(data.drop(['Revenue (Millions)', 'Metascore'], axis=1).head())

# Classify movies based on ratings


def rating_group(rating):
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'


# Lets apply this function on our movies data
# creating a new variable in the dataset to hold the rating category
data['Rating_category'] = data['Rating'].apply(rating_group)

print(data[['Title', 'Director', 'Rating', 'Rating_category']].head(5))
