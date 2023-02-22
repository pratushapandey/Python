#Linear Search
# Recursion

def linearSearch(arr,x,val):
    if arr[x] == val:
        return x
    elif x == -1:
        return -1
    return linearSearch(arr,x-1,val)


arr = [3,5,6,9,10,20]
x = len(arr)
val = int(input("Enter the element to be found: "))

print(x)
result = linearSearch(arr,x-1,val)

if result == -1:
    print("Item {} not found".format(val))
else:
