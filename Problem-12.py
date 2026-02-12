def min_jumps(arr):
    n = len(arr)

    
    if arr[0] == 0:
        return -1
    if n == 1:
        return 0

    max_reach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1, n):

        
        if i == n - 1:
            return jumps

        max_reach = max(max_reach, i + arr[i])

        
        steps -= 1

        
        if steps == 0:
            jumps += 1

            # If current index >= max_reach, cannot move further
            if i >= max_reach:
                return -1
            steps = max_reach - i

    return -1
