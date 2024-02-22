## Game of Life
This Python script simulates Conway's Game of Life using Pygame, a popular library for creating games and multimedia applications in Python. 
It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. The game is a classic example of emergent behavior and demonstrates how complex patterns can arise from simple rules.

## Installation and Setup
1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install Pygame by running `pip install pygame` in your terminal or command prompt.

## How to Play
- Upon running the script, the game window will appear, displaying the grid of cells.
- Click on the cells to toggle them between alive and dead states.
- Press any key to pause or resume the simulation.
- The initial configuration of cells has some predefined patterns including oscillating, moving, block, and oval cells.

## Rules of the Game
- Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Controls
- Click: Toggle cell alive/dead state.
- Any Key: Pause/Resume simulation.

## Features
- The game grid consists of a specified number of rows and columns.
- Cells can be toggled between alive and dead states using the mouse.
- The game continues to evolve according to the rules of Conway's Game of Life.
- Users can pause or resume the simulation at any time.

## Code Structure
- The script uses Pygame for creating the graphical interface and handling user inputs.
- The game state (cell grid) is represented using a numpy array.
- Cell evolution and drawing are handled within the `draw_cells()` function.
- The main loop controls the simulation and handles user inputs.

## Dependencies
- Python 3.x
- Pygame
- NumPy
