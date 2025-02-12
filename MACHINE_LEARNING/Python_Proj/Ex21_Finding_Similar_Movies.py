import pandas as pd
import csv
import os
import openpyxl

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")


m_cols = ['movie_id', 'title']
movies = pd.read_csv('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")
#print("\nMovies Data:")
#print(movies.head())

ratings = pd.merge(movies, ratings)

# Write the output to an Excel file
output_file = '/Users/sanjaybiswas/Documents/Pycharm/data/correlation_coefficient/similar_movies.xlsx'
ratings.to_excel(output_file,  sheet_name='UserRatings', index=False)

movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
print("\nPivot Table (Ratings by User and Movie):")
print(f"Pivot Columns : {movieRatings.columns}      \n values {movieRatings.head()}")

# Write movieStats to a new sheet in the existing Excel file
with pd.ExcelWriter(output_file, mode='a', engine='openpyxl') as writer:
    movieRatings.to_excel(writer, sheet_name='MovieRatings')

starWarsRatings = movieRatings['Star Wars (1977)']
print("\nStar Wars (1977):")
#starWarsRatings = starWarsRatings.dropna()
print(starWarsRatings.head())

similarMovies = movieRatings.corrwith(starWarsRatings)
print(similarMovies.head(10))

# Sort and assign back
similarMovies = similarMovies.sort_values(ascending=False)

# Convert to DataFrame for display
df = pd.DataFrame(similarMovies, columns=['Correlation'])
df.reset_index(inplace=True)
print("\nSimilar Movies:")
print(df)

df.rename(columns={'title': 'Movie'}, inplace=True)

# Write movieStats to a new sheet in the existing Excel file
with pd.ExcelWriter(output_file, mode='a', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Correlation')

print(f"\nOutput written to Excel file: {output_file}")

# Group by title and calculate size and mean
movieStats = ratings.groupby('title').agg({'rating': ['size', 'mean']})
print(movieStats.head())
movieStats.head()

# Write movieStats to a new sheet in the existing Excel file
with pd.ExcelWriter(output_file, mode='a', engine='openpyxl') as writer:
    movieStats.to_excel(writer, sheet_name='Movie Stats')

#Let's get rid of any movies rated by fewer than 100 people, and check the top-rated ones
popularMovies = movieStats['rating']['size'] >= 100
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]

with pd.ExcelWriter(output_file, mode='a', engine='openpyxl') as writer:
    movieStats[popularMovies].to_excel(writer, sheet_name='Rate_above_100_people')

# Updated for newer Pandas releases that don't allow merging between different levels; we must flatten it first now.
mappedColumnsMoviestat=movieStats[popularMovies]
mappedColumnsMoviestat.columns=[f'{i}|{j}' if j != '' else f'{i}' for i,j in mappedColumnsMoviestat.columns]
print(mappedColumnsMoviestat.head())
exit()
df = mappedColumnsMoviestat.join(pd.DataFrame(similarMovies, columns=['similarity']))

with pd.ExcelWriter(output_file, mode='a', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='RpopularMovies')

print(f"\nMovie stats written to a new sheet in: {df}")