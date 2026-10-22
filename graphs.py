def merge(arr1, arr2):
    #O(n), тк. в худшем случае мы пройдемся по каждому элементу изначального массива
    arr = []
    ind1 = 0
    ind2 = 0

    l = len(arr1) + len(arr2)

    for i in range(l):
        if ind1 > len(arr1) - 1:
                return arr+arr2[ind2:]
        if ind2 > len(arr2) - 1:
                return arr+arr1[ind1:]
        if arr1[ind1] <= arr2[ind2]:
            arr.append(arr1[ind1])
            ind1 += 1
        else:
            arr.append(arr2[ind2])
            ind2 += 1

    return arr

def merge_sort(arr):
    #O(log(n)), тк x = log2(n), х - кол во операций.
    if len(arr) != 1:
        h = len(arr)//2
        arr1 = arr[h:]
        arr2 = arr[:h]
        a = merge_sort(arr1)
        b = merge_sort(arr2)
    else:
        return arr
    return merge(a, b)

print(merge_sort([1, 9, 7, 5, 2, 4]))
#итоговая сложность - O(n * log(n))
