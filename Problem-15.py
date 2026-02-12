def merge_intervals(intervals):
    n = len(intervals)
    
    # Separate start and end arrays
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])

    merged = []
    start = starts[0]

    for i in range(1, n):
        # If next interval does NOT overlap
        if starts[i] > ends[i - 1]:
            merged.append([start, ends[i - 1]])
            start = starts[i]
    merged.append([start, ends[-1]])

    return merged


print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
print(merge_intervals([[1,4],[4,5]]))
print(merge_intervals([[4,7],[1,4]]))
