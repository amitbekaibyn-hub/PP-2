nums = [1,2,3,4]

#1example
print(list(map(lambda x: x*2, nums)))

#2example
print(list(map(lambda x: x**2, nums)))

#3example
print(list(map(lambda x: x+10, nums)))

#4example
print(list(map(lambda x: x-1, nums)))

#5example
print(list(map(lambda x: x%2==0, nums)))