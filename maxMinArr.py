#Method-1
def maxMin(arr):
    maxs = 0
    mins = 9999
    for i in arr:
        if i > maxs:
            maxs = i
        if i < mins:
            mins = i
    return maxs,mins

#Method-2
def maxMinusingSort(arr):
    arr.sort()
    return arr[-1],arr[0]

a,b=maxMinusingSort([1,2,3,4,5,68,7,6,5,7,8,9,22,33,44,55,100,4])
print(f"max {a} min {b}")
