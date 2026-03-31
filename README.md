# AI Puzzle Solver

Welcome to my **AI Puzzle Solver** project! As a student exploring the intersection of Artificial Intelligence and user experience, I built this application to show how a computer can "think" through a classic 3x3 sliding puzzle. 

My AI puzzle solve does not just make any random moves, the solver I made, uses a search strategy (specifically A* search algorithm) to find the shortest path from a mess of tiles to a perfect grid. 

## The Challenge  
The 8-puzzle (a 3x3 grid), consisting of eight numbered tiles and one empty slot. My goal was to find the most efficient sequence of moves to reach the goal state and not just "brute-force" guess it.  

## Key Features
* **Hands-on Interaction**: I made it like so that you can play the puzzle manually to test your own logic. I even made a shuffle button to randomize the board.
* **The "Brain" (A\* Algorithm)**: I implemented the A* search algorithm, which uses the Manhattan Distance heuristic to guarantee the shortest path to a solution.
* **Guided Solutions**: I made it such that even if you get stuck, the AI also gives the solution step-by-step.

## I Built it with:
* **Python**: The core language I used for all logic and search functions.  
* **Tkinter**: It is a Python library I used to create a clean, responsive Graphical User Interface (GUI).  
* **A\* Search & Heuristics**: It is the mathematical foundation that ensure the solver is both fast and optimal.  

## How can you try it:
1.  **Get the files**: Download/clone this repository to your computer.  
2.  **Launch the app**: Open your terminal or command prompt and run:  
    ```bash
    python main.py
    ```
3.  **Play & Shuffle**: Use the Shuffle button to shuffle the tiles, or move them yourself by clicking on them.  
4.  **Let the AI take over**: Click Solve to let the A* algorithm calculate the path.  
5.  **Learn the steps**: Use the Show steps button and next button to watch how the AI solved it.  

## Project Structure  
* **`main.py`**: This is like the heart of the user experience. It handles the buttons, the grid display, and the interaction logic.  
* **`solver.py`**: This is like the engine room. It contains the mathematical logic for the A* algorithm and the Manhattan Distance calculations.  

## Why I Built This?
I specially selected this problem because I feel this is like a perfect bridge between theory and practice. It allowed me to actually understand how "A* search algorithm" and "heuristics" work. I was even able to turn them into something visual and interactive. This project has deepened my understanding of how AI can be used to solve such problems effectively.  

## Known Limitations & Future Goals  
Currently, the solver is optimized for $3 \times 3$ grids, and very complex shuffles can sometimes cause the interface to pause while the AI "thinks". In the future, I plan to add:
* Smooth sliding animations for the tiles.
* Support for larger puzzles, such as $4 \times 4$ or $5 \times 5$ grids.
* A comparison tool to see how A* performs against other algorithms like BFS or DFS.
