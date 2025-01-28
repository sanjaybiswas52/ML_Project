import pandas as pd

# Define the data in JSON format 
data = {
    "student_id": [1, 1, 2, 2, 3, 3, 1, 2, 3],
    "subject": ["a", "b", "a", "b", "b", "a", "c", "c", "c"],
    "marks": [46, 98, 74, 50, 15, 35, 100, 29, 76]
}

# Create DataFrame
df = pd.DataFrame(data)

# Find the second-highest marks for each subject
second_highest = (
    df.sort_values(by=["subject", "marks"], ascending=[True, False])
    .groupby("subject")
    .nth(1)  # nth(1) gives the second row in each group
    .reset_index()
)

# Display the results
print(second_highest.to_string(index=False))

"""            SECOND METHOD
# Create a DataFrame
df = pd.DataFrame(data)

# Group by subject and calculate the second highest marks
def second_highest(series):
    unique_marks = series.unique()
    sorted_marks = sorted(unique_marks, reverse=True)
    return sorted_marks[1] if len(sorted_marks) > 1 else None

print(df.apply(second_highest).reset_index())
second_highest_marks = df.groupby('subject')['marks'].apply(second_highest).reset_index()
second_highest_marks.columns = ['subject', 'second_highest_marks']

# Print the results
print(second_highest_marks)

# Save the results to a CSV file
second_highest_marks.to_csv("second_highest_marks.csv", index=False)

#             THIRD METHOD
data = [
    (1, 'a', 46),
    (1, 'b', 98),
    (2, 'a', 74),
    (2, 'b', 50),
    (3, 'b', 15),
    (3, 'a', 35),
    (1, 'c', 100),
    (2, 'c', 29),
    (3, 'c', 76)
]

# Convert the data into a dictionary where the key is the subject and value is a list of marks
subject_marks = {}

for student_id, subject, marks in data:
    if subject not in subject_marks:
        subject_marks[subject] = []
    subject_marks[subject].append(marks)
    print(subject_marks[subject].append(marks))
    
print(subject_marks.items())
# Find the second highest marks for each subject
second_highest_marks = {}

for subject, marks in subject_marks.items():
    marks = sorted(set(marks), reverse=True)  # Remove duplicates and sort in descending order
    print(f" Marks : {marks}  Length Marks :{len(marks)}    Length Marks [1]:{marks[1]}\n")
    if len(marks) > 1:  # Ensure there are at least two unique marks
        second_highest_marks[subject] = marks[1]
        print(second_highest_marks[subject])
        print(second_highest_marks.items())
    else:
        second_highest_marks[subject] = None  # No second-highest if only one unique mark

# Print results
for subject, second_highest in second_highest_marks.items():
    print(f"Subject: {subject}, Second Highest Marks: {second_highest}")
    
"""