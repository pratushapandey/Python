# Binary Search
# Using Recursion


def binarySearch(arr,left,right,val):
    
    if(left <= right):
        mid = int(left + (right - left)/2)
        
        if arr[mid] == val:
            return mid
        elif val > arr[mid]:
            return binarySearch(arr,mid+1,right,val)
        else:
            return binarySearch(arr,left,mid-1,val)
    else:
        return -1


arr = [3,5,6,9,10,20]
x = len(arr)
val = 10

result = binarySearch(arr,0,x,val)

if result == -1:
    print("Element {} not found.".format(val))
else:
    print("Element {} found at position {}.".format(val,result))
