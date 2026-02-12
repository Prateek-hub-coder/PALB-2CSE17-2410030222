def max_subarray_sum(arr):
    n = len(arr)
    max_sum = arr[0]

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum > max_sum:
                max_sum = curr_sum

    return max_sum

arr = [2, 3, -8, 7, -1, 2, 3]
print("Maximum subarray sum:", max_subarray_sum(arr))
