"""learning loop
"""
for number1 in range(3):
    print("hello world", number1+1)

for number2 in range(1, 4):
    print("hello world", number2)


# for-else
SUCCESSFUL = False
for i in range(3):
    if SUCCESSFUL:
        print("successful")
        break
else:
    print("not successful")

NUMBER = 100
while NUMBER > 0:
    print(NUMBER)
    NUMBER //= 2
