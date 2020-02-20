def merge_sort(arr, aux, l, r):
    if l >= r - 1:
        return
    mid = int((l + r) / 2)
    merge_sort(arr, aux, l, mid)
    merge_sort(arr, aux, mid, r)
    merge(arr, aux, l, mid, r)


def merge(arr, aux, l, mid, r):
    aux[l:r] = arr[l:r].copy()
    j = l
    k = mid
    for i in range(r - l):
        if j >= mid:
            arr[l + i] = aux[k]
            k += 1
        elif k >= r:
            arr[l + i] = aux[j]
            j += 1
        elif aux[j] < aux[k]:
            arr[l + i] = aux[j]
            j += 1
        else:
            arr[l + i] = aux[k]
            k += 1


def sort(arr):
    aux = [0] * len(arr)
    l = 0
    r = len(arr)
    merge_sort(arr, aux, l, r)


data = [1, 1, 2, 7, 2, 4, 6, 8]
sort(data)
print(data)
