# Read the number of students
n = int(input())

# Initialize an empty dictionary to store student names and their marks
student_marks = {}

# Loop through the number of students and collect their marks
for _ in range(n):
    # Split the input into a list where the first element is the name and the rest are the marks
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))  # Convert marks to float
    student_marks[name] = marks

# Read the query name
query_name = input()

# Calculate the average marks of the queried student
average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])

# Print the average marks formatted to 2 decimal places
print(f"{average_marks:.2f}")
