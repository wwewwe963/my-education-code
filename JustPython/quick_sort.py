def quickSort(arr, start, end):
    if end > start:
        pivot = partition(arr, start, end)
        quickSort(arr, start, pivot - 1)
        quickSort(arr, pivot + 1, end)

def partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end

    while high > low:
        while arr[low] <= pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1

        if high > low:
            temp = arr[high]
            arr[high] = arr[low]
            arr[low] = temp
        
    while high > start and arr[high] >= pivot:
        high -= 1

    if pivot > arr[high]:
        arr[start] = arr[high]
        arr[high] = pivot
        return high
    else:
        return start

if __name__ == '__main__':
    arr = [12, 7, 5, 15, 10, 9, 4, 3, 1, 66, 7, 8, 3, 1, 3, 4, 5, 7, 3, 2]
    quickSort(arr, 0, len(arr) - 1)                                                                     
    print(arr)