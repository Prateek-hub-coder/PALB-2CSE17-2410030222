def find_median(arr):
    arr.sort()
    n = len(arr)
    
    if n % 2 == 1:   # Odd number of elements
        return arr[n // 2]
    else:            # Even number of elements
        return (arr[n//2 - 1] + arr[n//2]) / 2
