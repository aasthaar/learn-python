name = "Aastha"
print(type(name))
print(isinstance(name, str))

age = 21
print(isinstance(age, int))

# complex, set, float, bool, tuple, list, dict, range etc. are other data types in Python.

# if 1st argument if false and we are using 'OR' operator then 2nd argument will be considered, else first one.
print(False or []) #both false
print(False or 1)
print(1 or {})