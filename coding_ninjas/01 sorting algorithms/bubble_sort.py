# for an array of n items, n-1 iterations are required in bubble sort
# in each iteration, the smallest element is moved to left most end
# complexity of bubble sort is O(n**2) in worst case

def bubble_sort(array):

    n = len(array)
    if n==1:
        return
    
    for j in range(1,n):
        i = j-1
        while i >=0 and array[i] > array[i+1]:
            array[i],array[i+1] = array[i+1],array[i]
            i-=1
    return

print('enter input array:',end = '')
array = [int(x) for x in input().split()]

bubble_sort(array)

print('bubble sorted array:',array)
