# Prime Number
# Using Recursion

def prime_number(n, i = 2):
    if n % i == 0:
        return False
    elif n == i:
        return True
    prime_number(n, i+1)
    
    
n = int(input("Enter the number : "))

if prime_number(n):
    print("{} is a prime number".format(n))
else:
    print("{} is not a prime number".format(n))
