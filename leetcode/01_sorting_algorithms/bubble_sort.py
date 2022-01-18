# time complexity of bubble sort in worst case is O(n**2)

def bubble_sort(array):

    n = len(array)
    if n<=1:
        return

    for j in range(1,n):

        i = j-1

        while i >= 0 and array[i] > array[i+1]:
            array[i],array[i+1] = array[i+1],array[i]
            i-=1
    return

print('enter array to be sorted')
array = [int(x) for x in input().split()]
bubble_sort(array)
print('sorted array:')
print(array)

