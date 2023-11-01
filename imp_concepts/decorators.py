
# Decorators concept - Applying fucntions over functionw without changing the syntax

def uppertext_decorator(function):
    def wrapper(a,b):
        a = a.upper()
        b = b.upper()
        print(a)
        print(b)
        print("Calling- function")
        return function(a,b)

    return wrapper


def list_decorator(function):
    def wrapper(a,b):
        a = a
        b = b
        print("list_decorator called")
        print(str(a+b).split(' '))
    return wrapper

@uppertext_decorator
@list_decorator
def getString(a,b):
    print("function-called")
    return a+ " " +b

print(getString("hello","aditya"))
