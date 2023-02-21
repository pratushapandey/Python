#Largest element in an array

def largestElement(arr,x):
    if x == 1:
        return arr[0]
    return max(arr[x-1], largestElement(arr,x-1))


arr = [2,3,18,9,10]
x = len(arr)
print("Maximum Element : {}".format(largestElement(arr,x)))
