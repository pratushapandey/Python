# Bubble Sort - Normal Version


def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
def display(arr):
    print(" ".join(str(x)for x in arr))
                
                
arr = [28,6,4,2,24]
print("Before bubble sort:")
display(arr)

bubble_sort(arr)
print("After bubble sort:")
display(arr)
