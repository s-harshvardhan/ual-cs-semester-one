import random

def randQuicksort(arr):
   if len(arr) == 1 or len(arr) == 0:
       return arr
   else:
       pivot_index = random.randint(0, len(arr) - 1)
       pivot = arr[pivot_index]
       
       # Partition the array
       left = [x for x in arr if x < pivot]
       equal = [x for x in arr if x == pivot]
       right = [x for x in arr if x > pivot]
       
       # Recursively sort the left and right parts
       left = randQuicksort(left)
       right = randQuicksort(right)
       
       return left + equal + right

alist = [54,26,93,17,77,31,44,55,20]
print(randQuicksort(alist))
