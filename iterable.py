"iterables in python"
print(type(range(5)))  # range is an iterable
print(type("hello"))  # string is an iterable
print(type([1, 2, 3]))  # list is an iterable
print(type((1, 2, 3)))  # tuple is an iterable

# we can iterate ie use these types in loops
for char in "hello":
    print(char)
for num in range(5):
    print(num)
for item in ["a", "b", "c"]:
    print(item)
for element in (1, 2, 3):
    print(element)
