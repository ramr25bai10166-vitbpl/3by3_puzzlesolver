# AI Puzzle Solver

An artificial intelligence-based 3x3 Sliding Puzzle Solver. This project uses the A* search algorithm (with the Manhattan Distance heuristic) to find the optimal sequence of moves to solve a shuffled puzzle. It features a graphical user interface built with Python's standard `tkinter` library.

# Problem Statement

The classic 8-puzzle (a 3x3 sliding tile puzzle) problem consists of a 3x3 grid with 8 numbered square tiles and one blank space. Tiles can be moved into the blank space. The objective is to start from any reachable initial configuration and reach a specific goal configuration (typically tiles ordered 1 to 8 with the blank space at the bottom right) in the minimum number of moves.  

## Features
- **Interactive UI**: Play the puzzle manually or shuffle it randomly.
- **A\* Algorithm**: Gaurantees finding the shortest path to solve the puzzle.
- **Step-by-step Solution**: Visualizes each move required to reach the goal state.

## Prerequisites
- Python 3.x
- `tkinter` (usually included with standard Python installations)

## How to Run
1. Clone or download this project.
2. Run the main script:
   ```bash
   python main.py
   ```
3. Use the **Shuffle** button to randomize the board, or click the tiles to move them manually.
4. Click **Solve** to calculate the shortest path to the goal.
5. Step through the solution using the **Show steps** and **Next** buttons.

## Project Structure
- `main.py`: Contains the graphical user interface (GUI) logc using `tkinter`.
- `solver.py`: Contains the A* search algorithm and puzzle logic.  

# Project Objective

The main goal of this project is to develop a Python-based software application that solves the 8-puzzle problem using Artificial Intelligence. Specificly, the program implements the **A\* (A-star) search algorithm** employing the Manhattan Distance as a heuristic function to ensure an optimal solution.

# Scope  

1. **Algorithmic Module**: A solver engine that computes the shortest path between a given state and the goal state.
2. **Graphical User Interface (GUI)**: A user-friendly interface that allows users to manually interact with the puzzle, randomly shuffle the tiles, and request the solver to find the optimal path.
3. **Visualization**: A visual representation of the step-by-step solution.  

# Technologies Used

**Programming Language**: Python  
**GUI Framework**: tkinter  
**Algorithms**: A\* Search, Manhattan Distance Heuristic  

# Why this problem?
This problem was chosen because it is simple to understand but still demonstrates important AI concepts like state-space search, heuristics, and optimization.
