number_students = int(input())

students_record = {}

for i in range(number_students):
    name_grade = input().split()
    name = name_grade[0]
    grade = float(name_grade[1])
    if name not in students_record:
        students_record[name] = []
    students_record[name].append(grade)

for key, values in students_record.items():
    avg_grade = sum(values) / len(values)
    grades_as_str = " ".join(f"{grade:.2f}" for grade in values)
    print(f"{key} -> {grades_as_str} (avg: {avg_grade:.2f})")
