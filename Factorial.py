def factorial(num):
    if(n==1 or n==0):
        return 1
    else:
        if num > 1:
            return num * factorial(num-1)
        else:
            return 1


num = int(input("Enter the number : "))
print("The factorial of the number is: {}".format(factorial(num)))
