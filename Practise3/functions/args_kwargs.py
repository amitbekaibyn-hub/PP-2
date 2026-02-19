#1example
def sum_all(*args):
    return sum(args)

#2example
def print_all(*args):
    for i in args:
        print(i)

#3example
def info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

#4example
def student(name, *grades):
    print(name, sum(grades))

#5example
def combine(*args, **kwargs):
    print(args)
    print(kwargs)