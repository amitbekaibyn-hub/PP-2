students = [("Aibyn",18),("Ali",17),("Dana",19)]

#1example
print(sorted(students, key=lambda x: x[1]))

#2example
print(sorted(students, key=lambda x: x[0]))

#3example
print(sorted(students, key=lambda x: x[1], reverse=True))

#4example
nums = [5,2,9,1]
print(sorted(nums, key=lambda x: -x))

#5example
words = ["apple","kiwi","banana"]
print(sorted(words, key=lambda x: len(x)))