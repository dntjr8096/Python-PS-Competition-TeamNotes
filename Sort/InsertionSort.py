arr = [1, 5, 7, 3, 9]

for i in range(1, len(arr)):
    idx = i
    while arr[idx] < arr[idx-1] and idx >= 1:
        arr[idx-1], arr[idx] = arr[idx], arr[idx-1]
        idx -= 1

print(arr)

