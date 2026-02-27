#example 1
def mygenarator():
    yield 1
    yield 2
    yield 3
gen=mygenarator()
for i in gen:
    print(i)

#example 2
def numbers(n):
    for i in range(n):
        yield i
for num in numbers(5):
    print(num)

#example 3
def even_numbers(n):
    for i in range(n):
        if i%2==0:
            yield i
print(list(even_numbers(10)))

#example 4
class Myiterator():
    def __init__(self,max):
        self.max=max
        self.currenrt = 0
    def _iter_(self):
        return self
    
    def _next_(self):
        if self.currenrt<self.max:
            self.currenrt+=1
            return self.currenrt
        else:
            raise StopIteration
object=Myiterator(3)
for i in object:
    print(i)

#example 5

squares = (x*x for x in range(5))
for i in squares:
    print(i)