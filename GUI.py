import pygame
import random
import time

pygame.init() # start pygame

# Main class holding pygame object attributes
class DrawInfo:
    # RGB colors
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,0)
    RED = (255,0,0)
    GREEN = (128,128,128)
    BACKGOUND_COLOR = WHITE
    PERIPHERAL_PADDING = 100 # px
    TOP_PAD = 50
    
    # different shades of gray for bars
    BAR_SHADES = [(128,128,128),(160,160,160),(192,192,192)]
    
    def __init__(self, width, height, lst,lst_wrapper):
        self.width = width
        self.height = height
        self.lst = lst
        self.col_list = [self.BAR_SHADES[(index)%3] for index,_ in enumerate(lst)] # color assignment.
        self.lst_wrapper = lst_wrapper
        
        self.window =pygame.display.set_mode((width, height)) # main window
        
        pygame.display.set_caption("Navid's Sorting Visualization") # title
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('Press M for Merge Sort  B for Bubble Sort', True, self.GREEN, self.WHITE)
        textRect = text.get_rect()
        textRect.center = (300, 20)
        self.window.blit(text, textRect)
        self.set_list(lst)
        
    # sets main list and calculates needed 
    def set_list(self,lst):
        self.lst = lst
        # bounds for hight of histograms bars
        self.max_val = max(lst)
        self.min_val = min(lst)
        
        self.bar_width = ( self.width- DrawInfo.PERIPHERAL_PADDING) // len(lst) # width of each bar
        
        self.bar_height_scale_factor = ( self.height - DrawInfo.TOP_PAD ) // (self.max_val + self.min_val) # for scaling bar height        
        self.start_x = DrawInfo.PERIPHERAL_PADDING // 2
        
        
    def show_text(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
 
       
        text = font.render('Press M for Merge Sort  B for Bubble Sort', True, self.GREEN, self.WHITE)
        
        
        textRect = text.get_rect()
        
        
        textRect.center = (300, 20)
        self.window.blit(text, textRect)
        
    # screen update if mergesort was selected
    def merge_option(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('Resetting in 3 Seconds', True, self.BLACK, self.WHITE)
        textRect = text.get_rect()
        textRect.center = (300, 20)
        self.window.blit(text, textRect)
        pygame.display.update()
        time.sleep(3)
    
    # screen update if bubblesort was selected       
    def bubble_option(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('Resetting in 3 Seconds', True, self.BLACK, self.WHITE)
        textRect = text.get_rect()
        textRect.center = (300, 20)
        self.window.blit(text, textRect)
        pygame.display.update()
        time.sleep(3)