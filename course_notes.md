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

# Tuples vs List

1. Tuple is immutable while List is mutable
2. Tuple uses less resources!
3. List has a lot of functions

4. So try to use `Tuple` when dont need the functions of the list, and when dont need change it. 

