def rotate_using_temp(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    
    k = k % n
    temp = arr[-k:] + arr[:-k]
    return temp

print(rotate_using_temp([1,2,3,4,5,6,7], 10))
print(rotate_using_temp([1], 5))

def rotate_one_by_one(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    
    k = k % n
    
    for _ in range(k):
        last = arr[-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        arr[0] = last
    
    return arr

print(rotate_one_by_one([1,2,3,4,5,6,7], 10))
print(rotate_one_by_one([1], 5))

def rotate_reverse(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    
    k = k % n
    
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse(0, n-1)
    reverse(0, k-1)
    reverse(k, n-1)
    
    return arr

print(rotate_reverse([1,2,3,4,5,6,7], 10))
print(rotate_reverse([1], 5))
