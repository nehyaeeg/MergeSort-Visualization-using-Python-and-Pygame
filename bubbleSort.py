import pygame
from helpers import *
import time

def bubbleSort(lst,obj): #O(n^2)
    n = len(lst)
    for j in range(n-1):
        for i in range(n-1-j):
            
            # show 2 compared boxes in Red
            draw(obj)
            draw_list(obj)
            pygame.draw.rect(obj.window,obj.RED, ((obj.start_x + obj.bar_width*i),
                                                                      obj.height - obj.TOP_PAD - lst[i]*obj.bar_height_scale_factor,
                                                                      obj.bar_width, lst[i]*obj.bar_height_scale_factor))
            pygame.display.update()
            pygame.draw.rect(obj.window,obj.RED, ((obj.start_x + obj.bar_width*(i+1)),
                                                                      obj.height - obj.TOP_PAD - lst[(i+1)]*obj.bar_height_scale_factor,
                                                                      obj.bar_width, lst[(i+1)]*obj.bar_height_scale_factor))
            pygame.display.update()
            time.sleep(0.3)
            # bubble sort algorithm
            if lst[i] >= lst[i+1]:
                tmp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = tmp
                
            draw(obj) # clear screen
            draw_list(obj) # show list updated
    return lst