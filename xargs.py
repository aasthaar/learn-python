""" learn xargs ie variable parameters """


def multiply(*num):
    "multiply tuple"
    pdt = 1
    for numbers in num:
        pdt *= numbers
    print(pdt)


multiply(2, 3, 4, 6)
