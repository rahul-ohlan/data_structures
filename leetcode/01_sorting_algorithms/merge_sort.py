
from array import array


def merge(s1,s2,arr):

    if len(s1) == 0 or len(s2) == 0:
        return

    i,j,k = 0,0,0

    while i < len(s1) and j < len(s2):

        while i < len(s1) and s1[i] <= s2[j]:
            arr[k] = s1[i]
            i+=1
            k+=1
        if i >= len(s1):
            break
        while j < len(s2) and s2[j] < s1[i]:
            arr[k] = s2[j]
            j+=1
            k+=1
        if j >= len(s2):
            break
    
    while i < len(s1):
        arr[k] = s1[i]
        i+=1
        k+=1
    
    while j < len(s2):
        arr[k] = s2[j]
        j+=1
        k+=1
    
    return


def merge_sort(array):

    n = len(array)
    if n<=1:
        return

    mid = n//2
    s1 = array[0:mid]
    s2 = array[mid:n]

    merge_sort(s1)
    merge_sort(s2)

    merge(s1,s2,array)

    return

array = [1,0]
merge_sort(array)
print(array)