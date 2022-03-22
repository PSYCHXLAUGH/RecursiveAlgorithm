from sys import argv

def factorial(x):
    if x == 1: # base case
        return 1
    else: # recursive case
        return x * factorial(x - 1)

print(
    factorial(
        int(argv[1]) # input data
    )
)