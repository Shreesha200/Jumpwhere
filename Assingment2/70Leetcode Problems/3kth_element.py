def kth_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)