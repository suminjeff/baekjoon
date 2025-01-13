def find_largest_climb_size(n, heights):
    max_climb_size = 0
    current_start = None 

    for i in range(1, n):
        if heights[i] > heights[i - 1]:
            if current_start is None:
                current_start = heights[i - 1]
        else:
            if current_start is not None:
                max_climb_size = max(max_climb_size, heights[i - 1] - current_start)
                current_start = None

    if current_start is not None:
        max_climb_size = max(max_climb_size, heights[-1] - current_start)

    return max_climb_size

n = int(input()) 
heights = list(map(int, input().split()))  

print(find_largest_climb_size(n, heights))
