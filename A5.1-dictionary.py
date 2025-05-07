marks ={'Alice': 85,'Bob': 90,'Charlie': 78, 'Diana': 92}

name = input("Enter the student's name: ")

if name in marks:
    print("{}'s marks: {}".format(name,marks[name]))

else:
    print("Student not found.")