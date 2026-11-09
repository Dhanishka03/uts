# Get student details
name = input("Enter Student Name : ")
roll_no = input("Enter Student Roll No : ")

# Get subject marks
python = float(input("Enter Python Mark: "))
sql = float(input("Enter SQL Mark: "))
maths = float(input("Enter Mathematics Mark: "))

# Store subject names and marks in lists
subjects = ["Python", "SQL", "Mathematics"]
marks = [python, sql, maths]

# Calculate total marks using for loop
total = 0

for mark in marks:
    total = total + mark

# Calculate average
average = total / 3

# Check pass or fail
result = True

for mark in marks:
    if mark < 35:
        result = False

# Store student details in dictionary
student = {
    "Name": name,
    "Roll Number": roll_no,
    "Subjects": subjects,
    "Marks": marks,
    "Total": total,
    "Average": average,
    "Result": result
}

# Display student report
print("\n----- STUDENT REPORT -----")

print("Student Name:", student["Name"])
print("Roll Number:", student["Roll Number"])

print("\nSubject\t\tMark")

# Display subjects and marks using for loop
for i in range(len(subjects)):
    print(subjects[i], "\t\t", marks[i])

print("\nTotal Marks:", student["Total"])
print("Average:", round(student["Average"], 2))

# Display final result
if student["Result"] == True:
    print("Result: PASS")
else:
    print("Result: FAIL")
