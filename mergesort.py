from GUI import *
import time
from helpers import *

# Total O(n.log(n))
def mergesort(array,obj:DrawInfo): # this fucntion alone is O(Logn)
    
    # base case when array is un-half-able
    if len(array) <= 1:
        return array
    
    
    #divide to halves
    half_point = len(array) // 2
    #separate the halves
    left_array = array[:half_point]
    right_array = array[half_point:]
    
    left_array = mergesort(left_array,obj)
    right_array = mergesort(right_array,obj)
    
    return merge(array, left_array, right_array, obj)


def merge(array,left_array,right_array,obj): # this fucntion alone is O(n)
    
    i = 0 # left-array index
    j = 0 # right-array index
    
    final_array = []
    
    while len(final_array) < len(left_array) + len(right_array):
        draw(obj)
        draw_list(obj)
        
        pygame.draw.rect(obj.window,obj.RED, ((obj.start_x + obj.bar_width*left_array[i].old_index),
                                                                      obj.height - obj.TOP_PAD - left_array[i].value*obj.bar_height_scale_factor,
                                                                      obj.bar_width, left_array[i].value*obj.bar_height_scale_factor))
        pygame.display.update()
        
        pygame.draw.rect(obj.window,obj.RED, ((obj.start_x + obj.bar_width*right_array[j].old_index),
                                                                      obj.height - obj.TOP_PAD - right_array[j].value*obj.bar_height_scale_factor,
                                                                      obj.bar_width, right_array[j].value*obj.bar_height_scale_factor))
        pygame.display.update()
        time.sleep(0.3)
        
        if left_array[i].value <= right_array[j].value:
            final_array.append(left_array[i])
            i += 1
        else:
            final_array.append(right_array[j])
            j += 1
        
        if i >= len(left_array) or j >= len(right_array):
            
            final_array.extend(left_array[i:]) or final_array.extend(right_array[j:])
            break
        
    
    index = 999999999999
    for i in final_array:
        if i.old_index <= index:
            index = i.old_index
            
    for i in range(len(final_array)):
        final_array[i].old_index = index + i
    
        
    for i in range(len(final_array)):
        draw(obj)
        obj.lst[i+index] = final_array[i].value
        
        draw_list(obj)
        time.sleep(0.1)
        
        
    
    return final_array


# a= [3,5,1,2,6,8,19,11,15,4]

# print(mergesort(a))

        
    