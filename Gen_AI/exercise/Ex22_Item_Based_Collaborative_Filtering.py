import pandas as pd

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('/Users/sanjaybiswas/Documents/Pycharm/MLCourse/ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)
# Write the output to an Excel file
output_file = '/Users/sanjaybiswas/Documents/Pycharm/data/correlation_coefficient/MoviesRatings_Collaboratives.xlsx'
#with pd.ExcelWriter(output_file, mode='w', engine='openpyxl') as writer:
ratings.to_excel(output_file,  sheet_name='MoviesRatings', index=False)

userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
with pd.ExcelWriter(output_file, mode='a', engine='openpyxl') as writer:
    userRatings.to_excel(writer, sheet_name='UserRatings')

print(userRatings.head())