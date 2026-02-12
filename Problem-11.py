def get_min_diff(arr, k):
    n = len(arr)
    arr.sort()
    
    # Initial difference
    ans = arr[n-1] - arr[0]
    
    # Smallest and largest after first change
    small = arr[0] + k
    big = arr[n-1] - k
    
    if small > big:
        small, big = big, small
    
    for i in range(1, n-1):
        subtract = arr[i] - k
        add = arr[i] + k
        
        
        if subtract < 0:
            continue
        
        # No change needed
        if subtract >= small or add <= big:
            continue
        
        # Decide whether to update small or big
        if big - subtract <= add - small:
            small = subtract
        else:
            big = add
    
    return min(ans, big - small)



arr = [1, 5, 8, 10]
k = 2
print(get_min_diff(arr, k))   


arr = [3, 9, 12, 16, 20]
k = 3
print(get_min_diff(arr, k)) 
