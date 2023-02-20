# Fibonacci Series

def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num-1)+fibo(num-2)
    

n = int(input("Enter the number: "))
print("Fibonacci Series : {}".format(fibo(n)))    
