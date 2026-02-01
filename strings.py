"""
learn strings
"""

COURSE = "python Programming"
print(len(COURSE))  # length of the string
print(COURSE[0])    # first character
print(COURSE[-1])   # last character
print(COURSE[0:3])  # substring from index 0 to 2
print(COURSE[0:])   # substring from index 0 to end
print(COURSE[:5])   # substring from start to index 4
print(COURSE[:])    # whole string
print(COURSE[0:5:2])  # substring from index 0 to 4 with step 2
print(COURSE[::3])   # whole string with step 3
print(COURSE.upper())  # convert to uppercase
print(COURSE.lower())  # convert to lowercase
print(COURSE.find("Pro"))  # find substring
print(COURSE.replace("Programming", "Course"))  # replace substring
print("Python" in COURSE)  # check substring presence
print("python" in COURSE)  # case-sensitive check
print(COURSE.title())  # convert to title case
print(COURSE.split())  # split string into list
