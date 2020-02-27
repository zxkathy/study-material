def quick_sort(arr, l, r):
    if l >= r - 1:
        return
    k = r - 1
    i = l
    j = r - 2
    while i <= j:
        if arr[i] < arr[k]:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
    arr[i], arr[k] = arr[k], arr[i]
    quick_sort(arr, l, i)
    quick_sort(arr, i, r)

    
def sort(arr):
    quick_sort(arr, 0, len(arr))


arr = [1, 5, 3, 7, 6, 9, 0]
sort(arr)
print(arr)
