dict1 = {
    "one": 1,
    "two": "2"
}

print(dict1["one"])

print(dict1.get("KEY_THAT_NOT_EXIST"))

print(f"Keys of the dict: {dict1.keys()}")

print(f"Values of the dict: {dict1.values()}")

print(f"Keys+Values as tuple: {dict1.items()}")

print("Dict tuples:")
[print(f"{ item[0] }={ item[1] }") for item in dict1.items()]


[print(f"{ k }={ v }") for k, v in dict1.items()]


[dict1.__setitem__(k, None) for k in dict1.keys()]


print(f"Dict after cleaning {dict1}")

# Dict comprehension

print(f"Dict after cleaning { {k:None for k in dict1.keys()} }")
