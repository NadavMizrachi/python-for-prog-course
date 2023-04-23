# Strings

### raw string:

If we want to use the string "as is":

    raw_s = r"path/to/file and more words"

### Format variables in string:

    x = 1
    formatted_str = f" The value is {x}"

## Range in arr

We can "slice" strings/arrays from index to index.
example:
    
    str = "nadav"
    print(str[1:3]) # ad

It always until the (last_index - 1)

## Input from user

    in = input('please enter int')
    print(in)


# Check type of var

    x = "hi"
    type(x)

# Delete var from memory

    li = [1, 2, 3]
    def(li)

    # Now cant user li

# Immutable vs Mutable

There are objects that is immutable:

    s = "nadav"
    s[2] = 'a' # --> Exception
    
On the other hand, there are object that is mutable, for example, `list`.

Mutable:
    - list
    - dict
    - set

Immutable:
    - int
    - str
    - tuple
    - set
    - float


# Tuples vs List

1. Tuple is immutable while List is mutable
2. Tuple uses less resources!
3. List has a lot of functions

4. So try to use `Tuple` when don't need the functions of the list, and when don't need change it. 


# for, else

    for ...
    code
        if something...
            break
    else
        other code...

If for was stopped by `break` , the code in `else` will be executed. Otherwise, the code int the `else` won't 
be executed.

# Functions

## kwargs

    def func(**kwargs):
        ...

    func({key1: val1, key2: val2})

`kwargs` is actually a dictionary.

# Modules

Python file.

If we want to use the module, we need to import the module. For example:

    import <my-module>

Then we will be able to use functions defined in the module:

    <my-module>.func()

How python knows where to look for modules?
Python looks for in the directories that are listed in the variable `sys.path` (list of paths). Python first look in the
first path, then in the second and so on...
Python has few places it looks for modules. 
First it looks for modules in same directory.

## `__name__`

`__name__` is variable on any python module. 
If the module file executed directly, the content of `__name__` is `__main__`.
If the module is imported from another module, then the content of `__name__` is the name of the module file.

# Packages

Directory with `__init__.py` file. This directory contains modules. We can install this package in python envs. The
`__init__.py` file has different metadata infos about the package (such as version).


# Object Oriented

- constructor - implement `__init__` 
- toString = implement `__str__`
- String representation = implement __repr__
- `>` operator = implement `__gt__`
- `==` operator = implement `__eq__`
- `del()` (function that is being called before garbage collector destructs the object) = implement `__del__`
- `+` operator = implement `__add__`

## difference `__str__` and `__repr__'

`__str__` is for human readable string, while `__repr__` is more official Python string (could be JSON, 
or Python object form)

    class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

    p = Person("Alice", 30)
    
    print(p)          # Output: Alice (30)
    print(str(p))     # Output: Alice (30)
    print(repr(p))    # Output: Person('Alice', 30)

    
# Decorator

"Decorate" function with wrapped behaviour.

# Iterable 

Data structure that holds in the memory only one item at a time. When we call `next()` on
the iterable, then it proceeds to next item. For example, when we use `for` on
iterable, each iteration is calling `next()`. So the follow `for` has million iterations,
but for the all execution there is only one item in memory:


    for item in range(1_000_000):
        print(item)


We can create objects that are `iterables` by implementing `__iter__` and `__next__`.
`__iter__` should return `self`. 
`__next__` implements the logic that proceeds the items in iterations. When `__next__`
should stop, it raises stopIteration exception.

# Files

f = open('path/to/file')

`f` is generator (saves one chunk in memory).

# Close Resources:

When we done with file, we need to close it (`f.close()`)
In python there is special keyword, `with`, that will close when we finish use the file.

Example:

    with open('example.txt', 'r') as file:
        data = file.read()
        print(data)

In order to enable our object to be "closed" by `with`, we need to implement 2 methods, __enter__ 
and __exit__:


    class MyObject:
    def __init__(self):
        # initialize the object
        pass

    def __enter__(self):
        # return the object to be used in the with block
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # handle any necessary cleanup or error handling
        pass

# stdin & stdout & stderr

We can change the stdin/out/err (for example, redirect the output to a file)

    import sys

    f = open('errors.log' , 'a+')
    sys.stderr = f

# multiprocessing

We can assign python function to distinct processes.  For example:

    def sleepy_man(id):
    print(f'Process id {id} Starting to sleep...')
    time.sleep(1)
    print('Done sleeping')


    if __name__ == "__main__":
        tic = time.time()
        p1 = multiprocessing.Process(target=sleepy_man, args=(1,))
        p2 = multiprocessing.Process(target=sleepy_man, args=(2,))
        p1.start()
        p2.start()
    
        # Wait for process p1 to finish it's job
        p1.join()
    
        # Wait for process p2 to finish it's job
        p2.join()


We can use processes pool:

    def inc(x):
    return x ** 2
    
    if __name__ == "__main__":
    numbers = range(1, 10)
    my_pool = Pool(processes=cpu_count())
    outputs = my_pool.map(inc, numbers)
    print(outputs)


## share data between processes

### Pipe

We can send data between processes by using `Pipe` object

### Queue

We can send data between processes by `Queue` object.

# Threading 

There is Threading module.

## sync

We can syncronize threading with `Lock` object. 

# Multiprocessing and Threading

When we use multiprocessing and when we will use threading?

* When we use IO's, use threading.
* When we use heavy calculations, use multiprocessing.


# Subprocessing

We can open sub processes in our python program. For example, the next code will open the windows calculator:

    import subprocess
    x = subprocess.run('calc.exe')

How does the program knows what 'calc.exe' is? Because 'calc.exe' was set in path env variable.  