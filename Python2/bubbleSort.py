def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range (0,n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]

    return arr

arr = [64,36,78,34,86,32]
print(bubbleSort(arr))