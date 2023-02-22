#Linear Search
# Using loop

def linearSearch(arr,x,val):
    for i in range (0, x):
        if arr[i] == val:
            return i
    return -1
    
    
arr = [3,5,6,9,10,20]
x = len(arr)
val = int(input("Enter the element to be found: "))

print(x)
result = linearSearch(arr,x,val)

if result == -1:
    print("Item {} not found".format(val))
else:
    print("Item {} found at index {}".format(val,result))
