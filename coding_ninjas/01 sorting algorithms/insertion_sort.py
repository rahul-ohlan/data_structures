# we iterate on the given array
# for each element, move all the elements less than the element towards the right
# in the end, replace the blank space with the original element
# worst case time complexity = O(n**2)

def insertion_sort(array):

    n = len(array)
    if n==1:
        return
    
    for j in range(1,n):
        i = j-1
        temp = array[j]
        
        while i >= 0 and array[i]>temp:
            array[i+1] = array[i]
            i-=1
        array[i+1] = temp # replacing the blank space with array[j]
    return

print('enter array in as space separated input')
array = [int(x) for x in input().split()]

# sort the array
insertion_sort(array)
print('sorted array:',array)