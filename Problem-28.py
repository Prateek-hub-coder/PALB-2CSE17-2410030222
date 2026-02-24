def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m = len(matrix)
    n = len(matrix[0])
    
    low = 0
    high = m * n - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Convert 1D index to 2D
        row = mid // n
        col = mid % n
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False
