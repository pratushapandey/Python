def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)
      

num = int(input("Enter the number: "))
exp = int(input("Enter the exponent: "))

print("The power of the number {} is: {}".format(num,power(num,exp)))
