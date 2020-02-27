def max_heapify(arr, s, e):
    while s <= int((e - 1) / 2):
        left = s * 2 + 1
        right = s * 2 + 2
        lv = arr[left] if left < e else -100000
        rv = arr[right] if right < e else -10000
        if arr[s] < lv or arr[s] < rv:
            if lv >= rv:
                arr[s], arr[left] = arr[left], arr[s]
                s = left
            else:
                arr[s], arr[right] = arr[right], arr[s]
                s = right
        else:
            return


def make_heap(arr):
    n = len(arr)
    for i in range(int(n / 2), -1, -1):
        max_heapify(arr, i, n)


def heap_sort(arr):
    n = len(arr)
    make_heap(arr)
    print(arr)
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, 0, i)
        print(i, arr)


arr = [4, 2, 1, 5, 6, 7, 3]
make_heap(arr)
print(arr)

heap_sort(arr)
print(arr)
