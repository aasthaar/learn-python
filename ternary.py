# normal method
def check_adult(age):
    if(age>=18):
        print("Adult")
    else:
        print("Not Adult")

# ternary method
def check_age(age):
    return True if age>=18 else False

age=int(input("Enter your age: "))
result = check_age(age)
print(result)