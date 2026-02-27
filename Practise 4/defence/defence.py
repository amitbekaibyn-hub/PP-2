import json
with open("instroction.json", "r", encoding="utf-8") as f:
    instroction = json.load(f)
with open("students.json", "r",encoding="utf-8") as f:
    students = json.load(f)

course_map = {}
for t in instroction:
    course_map[t['course']] = {"teacher": t['name'], "students": []}

for s in students:
    if s['course'] in course_map:
        course_map[s['course']]["students"].append(s['name'])

for c, info in course_map.items():
    print(f"{info['teacher']} (Course {c}) студенттер:")
    for st in info['students']:
        print(st)