# algorithm:
# 1. take the key element to it's right position
# 2. get elements lower than the key element to the left and those greater on the right
# 3. Repeat recursively
# 4. worst case complexity is O(n**2)

from array import array


def partition(arr,si,ei,ki):

    if si >= ei:
        return

    while si < ei:
        if arr[si] < arr[ki]:
            si +=1

        elif arr[ei] > arr[ki]:
            ki -=1

        else:
            arr[si],arr[ei] = arr[ei],arr[si]
            si +=1
            ei -=1
        
    return

        



def quickSort(array,si,ei):

    if si >= ei:
        return

    if len(array) <=1:
        return

    # assume key element to be at si
    count = 0
    for i in range(si,ei+1):
        if array[i] < array[si]:
            count +=1
    
    # now we have number of elements less than the key element 
    key_index = si + count
    array[si],array[key_index] = array[key_index],array[si]

    # now modify the array to make smaller elements to the left of key index
    partition(array,si,ei,key_index)

    quickSort(array,si,key_index-1)
    quickSort(array,key_index+1,ei)
    
    return


array = [1,1,1]
si = 0
ei = len(array)-1
quickSort(array,si,ei)
print(array)

