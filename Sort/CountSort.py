arr = [1, 5, 7, 3, 9]

count = [0] * (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1

sorted_arr = []
for i in range(len(count)):
    tmp = [i] * count[i]
    sorted_arr.extend(tmp)

print(sorted_arr)