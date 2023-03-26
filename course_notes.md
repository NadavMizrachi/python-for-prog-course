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
- `>` operator = implement `__gt__`
- `==` operator = implement `__eq__`
- `del()` (function that is being called before garbage collector destructs the object) = implement `__del__`
- `+` operator = implement `__add__`
    