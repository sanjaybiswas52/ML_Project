import pandas as pd
import numpy as np

'''
KNN (K-Nearest-Neighbors)
As an example, let's look at the MovieLens data. We'll try to guess the rating of a movie by looking at the 10 movies
that are closest to it in terms of genres and popularity.
To start, we'll load up every rating in the data set into a Pandas DataFrame:
'''

# Load ratings data
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3))

# Write the output to an Excel file
output_file = '/Users/sanjaybiswas/Documents/Pycharm/data/correlation_coefficient/KNN.xlsx'

# Number of ratings for each movie by user
# Replace `np.size` and `np.mean` with their string equivalents
movieProperties = ratings.groupby('movie_id').agg({'rating': ['size', 'mean']})

# Normalize the number of ratings
movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
movieNormalizedNumRatings.head()

movieDict = {}
with open(r'/Users/sanjaybiswas/Documents/Pycharm/MLCourse/ml-100k/u.item', encoding="ISO-8859-1") as f:
    for line in f:
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)  # Convert genre fields to integers
        movieDict[movieID] = (
            name,
            np.array(list(genres)),
            movieNormalizedNumRatings.loc[movieID].get('size'),
            movieProperties.loc[movieID].rating.get('mean'),
        )

print(movieDict)