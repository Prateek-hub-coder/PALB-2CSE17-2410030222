def row_with_max_ones(arr):
    if not arr:
        return -1
    
    n = len(arr)
    m = len(arr[0])
    
    row_index = -1
    j = m - 1   
    
    for i in range(n):
        while j >= 0 and arr[i][j] == 1:
            row_index = i
            j -= 1
    
    return row_index
