#example 1
for i in range(1,6):
    print(i)


#example 2

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#example 3

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
   for y in fruits:
      print(x,y)