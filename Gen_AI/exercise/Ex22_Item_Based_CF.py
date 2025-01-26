"""
Item-Based Collaborative Filtering
Movies Recommendations based on User Ratings
"""

import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)
# Write the output to an Excel file
output_file = '/Users/sanjaybiswas/Documents/Pycharm/data/correlation_coefficient/MoviesRatings_Collaboratives.xlsx'

#Movie ratings by user
userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

#Each Movie has relation to each other based on user ratings
corrMatrix = userRatings.corr()

#Collrelation of movies where 100 people give ratings, If less than 100 people give ratings, then it will be ignored
corrMatrix = userRatings.corr(method='pearson', min_periods=100)
corrMatrix.head()

# My Ratings only
myRatings = userRatings.loc[0].dropna()

# Now let's go through each movie I rated one at a time, and build up a list of possible recommendations based on the movies 
# similar to the ones I rated.
simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print ("Adding sims for " + myRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[myRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myRatings[i])
    # Add the score to the list of similarity candidates
    simCandidates = pd.concat([simCandidates, sims])
    
#Glance at our results so far:
print ("sorting...")
simCandidates.sort_values(inplace = True, ascending = False)
print (simCandidates.head(10))

#For unique movie, similar to the ones I rated.
simCandidates = simCandidates.groupby(simCandidates.index).sum()
simCandidates.sort_values(inplace = True, ascending = False)

filteredSims = simCandidates.drop(myRatings.index)


with pd.ExcelWriter(output_file, mode='a', engine='openpyxl') as writer:
    filteredSims.to_excel(writer, sheet_name='filteredSims')

print(filteredSims.head())