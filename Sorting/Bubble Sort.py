# Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
                
def display(arr):
    print(" ".join(str(x)for x in arr))

    
arr = [10,20,30,40,50]
print("Before bubble sort:")
display(arr)

bubble_sort(arr)
print("After bubble sort:")
display(arr)
