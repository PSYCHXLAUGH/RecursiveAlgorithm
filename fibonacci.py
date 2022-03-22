from sys import argv

def fibonacci(x):
    if x == 1: # base case 
        return 0
    if x == 2:
        return 1
    else: # recursive case
        return fibonacci(x - 1) + fibonacci(x - 2)
    
print(
    fibonacci(
        int(argv[1]) # input data
    )
)