# AI Puzzle Solver

Welcome to my **AI Puzzle Solver** project! As a student exploring the intersection of Artificial Intelligence and user experience, I built this application to show how a computer can "think" through a classic 3x3 sliding puzzle. 

Instead of just making random moves, this solver uses a search strategy (specifically A* search algorithm) to find the shortest path from a mess of tiles to a perfect grid. 

## The Challenge  
The 8-puzzle (a 3x3 grid) is a classic benchmark in AI, consisting of eight numbered tiles and one empty slot. My goal was to move past "brute-force" guessing and create an intelligent agent that finds the **most efficient** sequence of moves to reach the goal state.

## Key Features
* **Hands-on Interaction**: You can play the puzzle manually to test your own logic or use the shuffle feature to randomize the board[cite: 110].
* **The "Brain" (A\* Algorithm)**: I implemented the A* search algorithm, which uses the Manhattan Distance heuristic to guarantee the shortest path to a solution.
* **Guided Solutions**: If you get stuck, the AI doesn’t just jump to the end—it visualizes each individual move so you can follow its logic step-by-step.

## Built With:
* **Python**: The core language used for all logic and search functions.  
* **Tkinter**: A standard Python library used to create a clean, responsive Graphical User Interface (GUI).  
* **A\* Search & Heuristics**: The mathematical foundations that ensure the solver is both fast and optimal.  

## How to Try It
1.  **Get the files**: Download or clone this repository to your computer.  
2.  **Launch the app**: Open your terminal or command prompt and run:  
    ```bash
    python main.py
    ```
3.  **Play & Shuffle**: Use the Shuffle button to scramble the tiles, or move them yourself by clicking on them.  
4.  **Let the AI take over**: Click Solve to let the A* algorithm calculate the path.  
5.  **Learn the steps**: Use the Show steps and Next buttons to watch the AI's "thought process" in action.  

## Project Structure  
* **`main.py`**: This is like the heart of the user experience. It handles the buttons, the grid display, and the interaction logic.  
* **`solver.py`**: This is like the engine room. It contains the mathematical logic for the A* algorithm and the Manhattan Distance calculations.  

## Why I Built This?
I chose this problem because it is a perfect bridge between theory and practice. It allowed me to take abstract concepts like "state-space search" and "heuristics" and turn them into something visual and interactive. This project has deepened my understanding of how AI can be used to solve optimization problems effectively.  

## Known Limitations & Future Goals  
Currently, the solver is optimized for $3 \times 3$ grids, and very complex shuffles can sometimes cause the interface to pause while the AI "thinks"[cite: 114]. In the future, I plan to add:
* Smooth sliding animations for the tiles.
* Support for larger puzzles, such as $4 \times 4$ or $5 \times 5$ grids.
* A comparison tool to see how A* performs against other algorithms like BFS or DFS.
