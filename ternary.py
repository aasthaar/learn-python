"""This module demonstrates the use of the ternary operator in Python"""
#normal method

# def check_adult(age1: Any) -> None:
#     if age1>=18:
#         print("Adult")
#     else:
#         print("Not Adult")

# ternary method
def check_age(age2):
    """This function checks if the person is adult or not using ternary operator."""
    return True if age2>=18 else False

age=int(input("Enter your age: "))
RESULT = check_age(age)
print (RESULT)
