#1 example
def number_square(n):
    for i in range(n):
        yield i*i
n=int(input())
for num in number_square(n):
    print(num)

#2 example
def even_numbers(n):
    for i in range(n+1):
        if i%2==0:
            yield i
for num in even_numbers(10):
    print(num)

#3 example
def boliny(n):
    for i in range(n):
        if i %3==0 and i%4==0:
            yield i
n=int(input())
for num in boliny(n):
    print(num)