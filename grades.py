students = {"John": 70, "Kelvin": 85, "Mercy": 60}

students_upper = {name.upper(): score for name, score in students.items()}

average_score = sum(students_upper.values()) / len(students_upper)

top_student = max(students_upper, key=students_upper.get)
top_score = students_upper[top_student]

print(f"Average Score: {average_score:.2f}")
print(f"Top Student: {top_student} ({top_score})")