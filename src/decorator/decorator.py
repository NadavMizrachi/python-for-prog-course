def my_decorator(func):
    def decorated_func():
        print("Doing something before func()...")
        func()
        print("Doing something after func()...")
        # do other thing...
    return decorated_func


@my_decorator
def my_func():
    print("In my_func()")


my_func()
