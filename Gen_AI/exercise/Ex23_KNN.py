import pandas as pd
import numpy as np

''' 
KNN (K-Nearest-Neighbors)
As an example, let's look at the MovieLens data. We'll try to guess the rating of a movie by looking at the 10 movies that are closest to it in terms of genres and popularity.

To start, we'll load up every rating in the data set into a Pandas DataFrame:
'''


r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3))

# Write the output to an Excel file
output_file = '/Users/sanjaybiswas/Documents/Pycharm/data/correlation_coefficient/KNN.xlsx'

#Number of ratings for each movie by user.
movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})

#The raw number of ratings isn't very useful for computing distances between movies, so we'll create a new DataFrame 
# that contains the normalized number of ratings. So, a value of 0 means nobody rated it, and a value of 
#1t means every body watch this movie and 0 means nobody watch this movie.

movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
movieNormalizedNumRatings.head()



movieDict = {}
with open(r'/Users/sanjaybiswas/Documents/Pycharm/MLCourse/ml-100k/u.item', encoding="ISO-8859-1") as f:
    temp = ''
    for line in f:
        #line.decode("ISO-8859-1")
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, np.array(list(genres)), movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))
        #print(f"Movie ID: {movieID} Name: {name} Genres: {genres} NumRatings: {movieNormalizedNumRatings.loc[movieID].get('size')} MeanRating: {movieProperties.loc[movieID].rating.get('mean')}")

print(movieDict[1])
#with pd.ExcelWriter(output_file, mode='a', engine='openpyxl') as writer:
    #movieNormalizedNumRatings.to_excel(writer, sheet_name='movieNormalizedNumRatings')

