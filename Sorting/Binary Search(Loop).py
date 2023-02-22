# Binary Search
# Using Loop


def binarySearch(arr,left,right,val):
    
    while(left <= right):
        mid = int(left + (right - left)/2)
        
        if arr[mid] == val:
            return mid
        elif val > arr[mid]:
            left = mid+1
        else:
            right = mid -1
    return -1

arr = [3,5,6,9,10,20]
x = len(arr)
val = 5

result = binarySearch(arr,0,x,val)

if result == -1:
    print("Element {} not found.".format(val))
else:
    print("Element {} found at position {}.".format(val,result))
