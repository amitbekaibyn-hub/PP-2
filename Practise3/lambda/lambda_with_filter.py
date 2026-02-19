nums = [1,2,3,4,5,6]

#1example
print(list(filter(lambda x: x%2==0, nums)))

#2example
print(list(filter(lambda x: x>3, nums)))

#3example
print(list(filter(lambda x: x<5, nums)))

#4example
print(list(filter(lambda x: x!=2, nums)))

#5example
print(list(filter(lambda x: x%3==0, nums)))