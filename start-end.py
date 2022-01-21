#Method-1

def first_last(target,arr):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i+1 < len(arr) and arr[i+1]==target:
                i += 1
            return [start,i]
    return [-1,-1]
  
  
  #Method-2
  
  def first_and_last(target,arr):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1,-1]
    beg = start(target,arr)
    end = last(target,arr)
    return [beg,end]
  
  def start(target,arr):
    if arr[0] == target:
        return 0
    beg,end = 0,len(arr)-1
    while beg <= end:
        mid = (beg+end)//2
        if arr[mid] == target and arr[mid-1]<target:
            return mid
        elif arr[mid]<target:
            beg = mid+1
        else:
            end = mid-1
    return -1
  
  def last(target,arr):
    if arr[-1] == target:
        return len(arr)-1
    beg,end = 0,len(arr)-1
    while beg <= end:
        mid = (beg+end)//2
        if arr[mid] == target and arr[mid+1]>target:
            return mid
        elif arr[mid]>target:
            end = mid-1
        else:
            beg = mid+1
    return -1
  
  
  print(first_and_last(5,[1,2,3,5,5,5,5,5,5,5,5,5,5,6,7,8]))    #[3,12]
  print(first_last(5,[1,2,3,5,5,5,5,5,5,5,5,5,5,6,7,8]))      #[3,12]
