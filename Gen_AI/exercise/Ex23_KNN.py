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
movieProperties = ratings.groupby('movie_id').agg({'rating': ['size', 'mean']})

#The raw number of ratings isn't very useful for computing distances between movies, so we'll create a new DataFrame 
# that contains the normalized number of ratings. So, a value of 0 means nobody rated it, and a value of 
#1t means every body watch this movie and 0 means nobody watch this movie.

movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))

movieDict = {}
#r_cols = ['MovieId', 'Name', 'Release', 'Filer', 'Url', 'Adventure', 'Comedy', 'Horror', 'Romance', 'Drama', 'Science_fiction', 'Thriller', 'Suspense', 'Sports', 'Western', 'Musical', 'Documentary', 'Action', 'Fantasy', 'Historical', 'Melodrama', 'Pornographic', 'Noir', 'Pure_hybrid']
with open(r'/Users/sanjaybiswas/Documents/Pycharm/MLCourse/ml-100k/u.item', encoding="ISO-8859-1") as f:
    temp = ''
    for line in f:
        #line.decode("ISO-8859-1")
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = ( name, np.array(list(genres)), movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))
        #print(f"Movie ID: {movieID} Name: {name} Genres: {genres} NumRatings: {movieNormalizedNumRatings.loc[movieID].get('size')} MeanRating: {movieProperties.loc[movieID].rating.get('mean')}")
        

#print(movieDict[1])
# MovieID          : 1
# Name             :'Toy Story (1995)', a
# Genre list       : [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Popularity score : 0.7735849056603774
# Average Rate     : 3.8783185840707963

from scipy import spatial

#Now let's define a function that computes the "distance" between two movies based on how similar their genres are, and 
# how similar their popularity is. Just to make sure it works, we'll compute the distance between movie ID's 2 and 4:
def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)
    popularityA = a[2]
    popularityB = b[2]
    popularityDistance = abs(popularityA - popularityB)
    return genreDistance + popularityDistance

print(movieDict[2])
print(movieDict[4])
ComputeDistance(movieDict[2], movieDict[4])
print(f"\nDistance between 2 and 4: {ComputeDistance(movieDict[2], movieDict[4])}\n")
#Distance between 2 and 4: 0.8004574042309892

#'GoldenEye (1995)', array([0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]), np.float64(0.22298456260720412), np.float64(3.2061068702290076))
#(Get Shorty (1995)', array([0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), np.float64(0.3567753001715266), np.float64(3.550239234449761))
# Distance between 2 and 4: 0.8004574042309892


import operator

#Now, we just need a little code to compute the distance between some given test movie (Toy Story, in this example) and 
# all of the movies in our data set. When the sort those by distance, and print out the K nearest neighbors:

def getNeighbors(movieID, K):
    distances = []
    for movie in movieDict:
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors

K = 10
avgRating = 0
neighbors = getNeighbors(1, K)
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print (movieDict[neighbor][0] + " " + str(movieDict[neighbor][3]))
    
avgRating /= K

#with pd.ExcelWriter(output_file, mode='a', engine='openpyxl') as writer:
    #movie_genre.to_excel(writer, sheet_name='movie_genre')
