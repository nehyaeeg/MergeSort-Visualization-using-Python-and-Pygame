from mergesort import *
import pygame
from GUI import DrawInfo
from helpers import draw, draw_list, random_number_generator
import time
from bubbleSort import *


def main():
    
    n = 20 # number of bars    
    lst, lstwrapper = random_number_generator(n,1,100) # random initialization
    game_screen = DrawInfo(600,600,lst,lstwrapper) # initialize main pygame obj
    draw_list(game_screen) # show list
    pygame.time.Clock().tick(60)
    cont=True # variable for main loop control(backup)
        
    while cont:
        
        game_screen.show_text() #shpw starting instructions
        draw_list(game_screen) # show the list to be sorted
        
        pygame.display.update()
        for event in pygame.event.get(): # interaction
            draw_list(game_screen)
            if event.type == pygame.QUIT:
                cont == False
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    game_screen.lst = bubbleSort(game_screen.lst,game_screen) # perform and show
                    game_screen.bubble_option() # show resetting text
                    game_screen.lst, game_screen.lst_wrapper =  random_number_generator(n,1,100) # update list
                        
                if event.key == pygame.K_m:
                    game_screen.lst = mergesort(game_screen.lst_wrapper,game_screen) # perform and show
                    game_screen.bubble_option() # show resetting text
                    game_screen.lst, game_screen.lst_wrapper =  random_number_generator(n,1,100) # update list  
                    
if __name__ == "__main__":
    main()