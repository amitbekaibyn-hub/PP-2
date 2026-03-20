import os
from functools import reduce

students = []

folder = "scores"

files = os.listdir(folder)

for file in files:
    if file.endswith("s.txt"):
        with open(os.path.join(folder, file), "r") as f:
            for line in f:
                name, score = line.strip().split(",")
                students.append((name, int(score))) 

names = [s[0] for s in students]
scores = [s[1] for s in students]

total_students = len(students)

total_score = sum(scores)

average_score = total_score / total_students

highest = max(scores)
lowest = min(scores)

updated_scores = list(map(lambda x: x + 5, scores))

top_students = list(filter(lambda s: s[1] > 85, students))

product_scores = reduce(lambda a, b: a * b, scores)

print("Students with index:")
for i, (name, score) in enumerate(students, start=1):
    print(i, name, score)

combined = list(zip(names, scores))
print("\nCombined:", combined)
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print("\nSorted:")
for name, score in sorted_students:
    print(name, score)

with open("report.txt", "w") as f:
    f.write(f"Total students: {total_students}\n")
    f.write(f"Average score: {average_score}\n")
    f.write(f"Highest score: {highest}\n")
    f.write(f"Lowest score: {lowest}\n\n")

    f.write("Top students (>85):\n")
    for name, score in top_students:
        f.write(f"{name} {score}\n")