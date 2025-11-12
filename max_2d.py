def max(arr):
    max_val = arr[0][0]
    for row in arr:
        for num in row:
            if num > max_val:
                max_val = num
    return max_val

m = max([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)
