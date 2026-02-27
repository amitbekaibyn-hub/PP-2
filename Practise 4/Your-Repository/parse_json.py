import json

# Файлдарды оқу
teachers = json.load(open("instroduction.json", encoding="utf-8"))
students = json.load(open("students.json", encoding="utf-8"))

# Курстар бойынша байланыстыру
course_map = {}
for t in teachers:
    course_map[t['course']] = {"teacher": t['name'], "students": []}

for s in students:
    if s['course'] in course_map:
        course_map[s['course']]["students"].append(s['name'])

# Нәтижені шығару
for c, info in course_map.items():
    print(f"{info['teacher']} (Course {c}) оқитын студенттер:")
    for st in info['students']:
        print(" -", st)
    print()