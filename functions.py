"""learn functions"""


def greeting():
    """prints hello"""
    print("hello")


greeting()


# pass parameters
def greet_with_parameter(first_name, last_name):
    """greets with parameter"""
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(f"hello {first_name} {last_name}")


greet_with_parameter("Aastha", "Rai")
