arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

arr.sort()
print(arr[k-1])


#another way

arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
n = len(arr)

for i in range(n):
    count = 0
    for j in range(n):
        if arr[j] < arr[i]:
            count += 1

    if count == k - 1:
        print(arr[i])
        break

