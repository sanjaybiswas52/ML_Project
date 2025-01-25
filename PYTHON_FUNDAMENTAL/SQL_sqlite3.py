import sqlite3
import pandas as pd

# File paths
file1 = '/Users/sanjaybiswas/Documents/Pycharm/data/correlation_coefficient/movies.csv'  # Replace with your first CSV file path
file2 = '/Users/sanjaybiswas/Documents/Pycharm/data/correlation_coefficient/ratings.csv'  # Replace with your second CSV file path

# Load CSV files into pandas DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Create an in-memory SQLite database
conn = sqlite3.connect(":memory:")

# Load DataFrames into the database as tables
df1.to_sql('moives', conn, index=False, if_exists='replace')
df2.to_sql('ratings', conn, index=False, if_exists='replace')

# SQL query to perform an INNER JOIN on the 'id' column
query = """
SELECT r.user_id, m.movie_id, m.title, r.rating
FROM moives m inner join ratings r on (m.movie_id = r.movie_id)
"""

# Execute the query and fetch the result
ratings = pd.read_sql_query(query, conn)
movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

starWarsRatings = movieRatings['Star Wars (1977)']
similarMovies = movieRatings.corrwith(starWarsRatings)
df = pd.DataFrame(similarMovies, columns=['Correlation'])

output_file = '/Users/sanjaybiswas/Documents/Pycharm/data/correlation_coefficient/similar(Star_Wars_1977)movies_ratings.csv'
try:
    # Save the DataFrame to a new CSV file
    df.to_csv(output_file, index=False)  # `index=False` excludes the index column
    print(f"Data written successfully to {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")

exit()
clear()

# Display the result
print("Joined Data:")
print(result)