# AI Puzzle Solver

An artificial intelligence-based 3x3 Sliding Puzzle Solver. This project uses the A* search algorithm (with the Manhattan Distance heuristic) to find the optimal sequence of moves to solve a shuffled puzzle. It features a graphical user interface built with Python's standard `tkinter` library.

## Features
- **Interactive UI**: Play the puzzle manually or shuffle it randomly.
- **A* Algorithm**: Gaurantees finding the shortest path to solve the puzzle.
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
