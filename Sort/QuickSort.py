arr = [1, 5, 7, 3, 9, 1, 2]

def quickSort(arr, start, end):
    if start >= end:
        return

    pivot = arr[start]
    left = start+1
    right = end

    while left <= right:

        while pivot >= arr[left] and left <= end:
            left += 1

        while pivot < arr[right] and right > start:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[right], arr[start] = arr[start], arr[right]

    quickSort(arr, start, right-1)
    quickSort(arr, right+1, end)

quickSort(arr, 0, len(arr)-1)
print(arr)