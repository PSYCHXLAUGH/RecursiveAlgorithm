from sys import argv

def palindrome(string): # find palindrome strings
    if len(string) <= 1: # base case
        return True
    if string[0] != string[-1]: # base case
        return False
    else: # recursive case
        return palindrome(string[1:-1])

print(
    palindrome(
        argv[1] # input data
    )
)