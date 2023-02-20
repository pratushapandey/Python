# Sum Of Natural Number

def sum(num):
    if num <= 1:
        return num
    else:
        return num+sum(num-1)
    
    
n = int(input("Enter the number: "))
print("The sum of natural number: {}".format(sum(n)))
