
from heapq import merge
from turtle import right


def mergesort(array):
    
    # base case when array is un-half-able
    if len(array) <= 1:
        return array
    
    #divide to halves
    half_point = len(array) // 2
    #separate the halves
    left_array = array[:half_point]
    right_array = array[half_point:]
    
    left_array = mergesort(left_array)
    right_array = mergesort(right_array)
    
    return merge(left_array,right_array)


def merge(left_array,right_array):
    
    i = 0 # left-array index
    j = 0 # right-array index
    
    final_array = []
    while len(final_array) < len(left_array) + len(right_array):
        
        if left_array[i] <= right_array[j]:
            final_array.append(left_array[i])
            i += 1
        else:
            final_array.append(right_array[j])
            j += 1
        
        if i >= len(left_array) or j >= len(right_array):
            
            final_array.extend(left_array[i:]) or final_array.extend(right_array[j:])
            break
        
    return final_array


# a= [3,5,1,2,6,8,19,11,15,4]

# print(mergesort(a))

        
    