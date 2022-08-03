import pygame
from pygame.locals import *
import numpy as np

pygame.init()


## Screen specifications
HEIGHT, WIDTH = 800, 1000

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (30, 30, 30)

FPS = (30)

## Cells specifications
NxC, NyC = 120, 120

dim_NxC = WIDTH / NxC
dim_NyC = HEIGHT / NyC 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Life Game')



def draw_cells(NyC, NxC, cell_state, new_cell_state):

    for y in range(0, NyC):
        for x in range(0, NxC):

            ## Identify the neighborhood of the cell
            cell_neighbors = cell_state[(x-1) % NxC, (y-1) % NyC] + \
                            cell_state[(x)   % NxC, (y-1) % NyC] + \
                            cell_state[(x+1) % NxC, (y-1) % NyC] + \
                            cell_state[(x-1) % NxC, (y)   % NyC] + \
                            cell_state[(x+1) % NxC, (y)   % NyC] + \
                            cell_state[(x-1) % NxC, (y+1) % NyC] + \
                            cell_state[(x)   % NxC, (y+1) % NyC] + \
                            cell_state[(x+1) % NxC, (y+1) % NyC]
            
            ## Cell Rules
            ## N1:
            if cell_state[x, y] == 0 and cell_neighbors == 3:
                new_cell_state[x, y] = 1

            ## N2:
            elif cell_state[x, y] == 1 and (cell_neighbors < 2 or cell_neighbors > 3):
                new_cell_state[x, y] = 0 

            ## Create each cell(polygon)    
            cell = [(x *     dim_NxC, y *     dim_NyC),
                    (x *     dim_NxC, (y+1) * dim_NyC),
                    ((x+1) * dim_NxC, (y+1) * dim_NyC),
                    ((x+1) * dim_NxC, y *     dim_NyC)]


            if new_cell_state[x, y] == 0:
                pygame.draw.polygon(screen, (GREY), cell, 1)

            else:
                pygame.draw.polygon(screen, (WHITE), cell, 0)



def main():
    cell_state = np.zeros((NxC, NyC))

    current_time = 0
    initial_time = 0

    cell_state[5, 3] = 1
    cell_state[5, 4] = 1
    cell_state[5, 5] = 1

    cell_state[21, 21] = 1
    cell_state[22, 22] = 1
    cell_state[22, 23] = 1
    cell_state[21, 23] = 1
    cell_state[20, 23] = 1
    
    clock = pygame.time.Clock()
    
    run_condition = True

    pause_key = False

    ## Cell status
    cell_state = np.copy(cell_state)
    new_cell_state = np.copy(cell_state)
    
    while run_condition:
        clock.tick(FPS)

        ## Redraw the backgrownd of the screen
        screen.fill(BLACK)

        ## Controls
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run_condition = False
            
            if event.type == pygame.KEYDOWN:
                pause_key = not pause_key

            if sum(pygame.mouse.get_pressed()) > 0:
                pos_x, pos_y = pygame.mouse.get_pos()
                cel_x, cel_y = int(np.floor(pos_x/ dim_NxC)), int(np.floor(pos_y/ dim_NyC))
                new_cell_state[cel_x, cel_y] = 1
                print(pos_x, pos_y) ##_---------------------problems

            
            
            

                
        current_time = pygame.time.get_ticks()

        if current_time - initial_time > 200:

            if not pause_key:
                draw_cells(NyC, NxC, cell_state, new_cell_state)

                cell_state = np.copy(new_cell_state)

                pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()