import random
import pygame
from GUI import DrawInfo

# wrapper class used in mergesort drawing
# keeps value and old index for incremental
# update of the list
class int_obj:
    
    def __init__(self, old_index:int,value):
        self.old_index = old_index
        self.value = value
        
    def __repr__(self) -> str:
        return f"{self.old_index},{self.value}"
    
# generates random list 
def random_number_generator(n,min_value,max_value):
    
    lst =[]
    for _ in range(n):
        lst.append(random.randint(min_value,max_value))
    lst_wrapped = [int_obj(i,v) for i,v in enumerate(lst)]
        
    return lst, lst_wrapped
    
# Clear the screen 
def draw(draw_info : DrawInfo):
    draw_info.window.fill(draw_info.BLACK)
    pygame.display.update()
    
# Draw the list bars
def draw_list(draw_info : DrawInfo):
    lst = draw_info.lst
    x_vals = []
    height_vals = [i *draw_info.bar_height_scale_factor for i in lst]# list values scaled
    
    for index, value in enumerate(lst):
        x_vals.append(draw_info.start_x + draw_info.bar_width*index) # start index of each bar base + offset
        # draw each box 
        pygame.draw.rect(draw_info.window,draw_info.col_list[index], 
                         (x_vals[index], draw_info.height - draw_info.TOP_PAD - height_vals[index], 
                          draw_info.bar_width,height_vals[index]))
        pygame.display.update()