# Insertion Sort

def insertion_sort(arr):
    for i in range (1,len(arr)):
        
        temp = arr[i]
        j = i - 1
        
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

arr = [28,6,4,2,24]
print("Before insertion sort:")
print(arr)

insertion_sort(arr)
print("After insertion sort:")
print(arr)
