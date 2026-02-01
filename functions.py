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
# optional parameters must be placed after the required parameters only!!


def greet_with_optional_parameter(name, location="Earth"):
    """greets with optional parameter"""
    print(f"hello {name} from {location}")


greet_with_optional_parameter("Aastha")
greet_with_optional_parameter("Aastha", "India")
