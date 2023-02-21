# Printing Elements Using Recursion

def printValue(arr,size,i):
    
    if i == size:
        return 
    print(arr[i],end= " ")
    
    x = printValue(arr,size,i+1)
    return x


arr = [3,5,7,2,4,5]
size = len(arr)
i = 0
print(arr," ",size)
printValue(arr,size,i)
