# TO-DO: complete the helper function below to merge 2 sorted arrays
# this got rediculously long. Theres no way there isn't a better option
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = []
#     if len(arrA) == 0 or len(arrB) == 0:
#         return arrA if len(arrA) != 0 else arrB
#     # Your code here
#     i, j = 0, 0
#     while i < len(arrA) or j < len(arrB):
#         if arrA[i] < arrB[j]:
#             merged_arr.append(arrA[i])
#             if i < len(arrA)-1:
#                 i += 1
#             else:
#                 for b in range(j, len(arrB)):
#                     merged_arr.append(b)
#         else:
#             merged_arr.append(arrB[j])
#             if j < len(arrA)-1:
#                 j += 1
#             else:
#                 for a in range(i, len(arrA)):
#                     merged_arr.append(a)
#     print(f'returning merged {merged_arr}')
#     return merged_arr

from random import randint


def merge(arr1, arr2):
    elements = len(arr1) + len(arr2)
    merged_arr = [0] * elements
    i = 0
    j = 0
    for m, _ in enumerate(merged_arr):
        if len(arr1) > i and len(arr2) > j:
            if arr1[i] > arr2[j]:
                merged_arr[m] = arr2[j]
                j += 1
            else:
                merged_arr[m] = arr1[i]
                i += 1
        else:
            if len(arr1) > i:
                merged_arr[m] = arr1[i]
                i += 1
            else:
                merged_arr[m] = arr2[j]
                j += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION

# Hmm. Evidence Sugests that this is quicksort not merge sort
def quick_sort(arr):
    # Your code here
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
            return arr
        else:
            return arr
    elif len(arr) > 2:
        mid = randint(0, len(arr))
        low = [i for i in arr if i <= arr[mid]]
        high = [i for i in arr if i > arr[mid]]
        low = quick_sort(low)
        high = quick_sort(high)
    elif len(arr) < 2:
        return arr
    arr = merge(low, high)

    return arr

# Merge Sort for real:


def merge_sort(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
            return arr
        else:
            return arr
    elif len(arr) > 2:
        mid = len(arr)//2
        low = arr[:mid]
        high = arr[mid:]
        low = merge_sort(low)
        high = merge_sort(high)
    elif len(arr) < 2:
        return arr
    arr = merge(low, high)
    return arr

# implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1

    while start2 <= end:
        if arr[start] > arr[start2]:
            print(f'before switch: {arr}')
            arr.insert(start, arr[start2])
            del arr[start2 + 1]
            print(f'after switch: {arr}')
            print(f'start: {start}, start2: {start2}')
            start2 += 1
            start += 1
        else:
            print(f'before other switch {arr}')
            arr.insert(start + 1, arr[start2])
            del arr[start2 + 1]
            print(f'after other switch {arr}')
            start += 2
            start2 += 1
            print(f'start: {start}, start2: {start2}')

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        mid = l + (r-l) // 2
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid+1, r)
        merge_in_place(arr, l, mid, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr


if __name__ == '__main__':
    arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    arr2 = [2, 4, 6, 8]
    arr3 = [1, 3, 5, 7, 9, 10, 2, 4, 6, 8]
    print(merge_sort_in_place(arr1, 0, len(arr1)-1))
