# time complexity for insertion sort is O(n**2)

def insertion_sort(array):

    n = len(array)
    if n<=1:
        return

    for j in range(1,n):
        temp = array[j]
        i = j-1

        while i >=0 and array[i] >= temp:
            array[i+1] = array[i]
            i-=1

        array[i+1] = temp
    return

print('enter array to be sorted:')
array = [int(x) for x in input().split()]
insertion_sort(array)
print('sorted array:')
print(array)
