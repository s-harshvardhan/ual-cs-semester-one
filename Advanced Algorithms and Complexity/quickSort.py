def quicksort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        pivot = arr[0]
        i = 0
        for j in range(len(arr)-1):
            if arr[j+1] < pivot:
                arr[j+1], arr[i+1] = arr[i+1], arr[j+1]
                i += 1
                print(arr)
        arr[0], arr[i] = arr[i], arr[0]
        first_part = quicksort(arr[:i])
        second_part = quicksort(arr[i+1:])
        first_part.append(arr[i])
        return first_part + second_part

alist = [54,26,93,17,77,31,44,55,20]
print(quicksort(alist))