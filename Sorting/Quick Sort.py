# Quick Sort

def partition(arr, low, high):
    swapIndex = low-1
    pivot = arr[high]
    
    for j in range(low,high):
        
        if arr[j] < pivot:
            swapIndex += 1
            arr[j],arr[swapIndex] = arr[swapIndex],arr[j]
            
    arr[swapIndex+1],arr[high] = arr[high],arr[swapIndex+1]
    
    return swapIndex+1


def quick_sort(arr,low,high):
    if low < high:
        indexPI = partition(arr,low,high)
        
        quick_sort(arr,low,indexPI-1)       #left partition
        quick_sort(arr,indexPI+1,high)      #right partition


arr = [70,90,10,30,50,20,60]
n = len(arr)

print(arr)

quick_sort(arr,0,n-1)

print(arr)
