# Last Occurance In An Array Using Recursion

def findValue(arr,i,val):
    
    if i == len(arr):
        return

    if arr[i] == val:
        return i
    
    x = findValue(arr,i-1,val)
    return x


arr = [3,5,7,2,4,5]
val = 5
i = len(arr)-1
findValue(arr,i,val)
