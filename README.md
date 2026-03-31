# AI Puzzle Solver

Welcome to my **AI Puzzle Solver** project! As a student exploring the intersection of Artificial Intelligence and user experience, I built this application to show how a computer can "think" through a classic 3x3 sliding puzzle. 

Instead of just making random moves, this solver uses a search strategy (specifically A* search algorithm) to find the shortest path from a mess of tiles to a perfect grid. 

## The Challenge  
The 8-puzzle (a 3x3 grid) is a classic benchmark in AI, consisting of eight numbered tiles and one empty slot[cite: 97, 98]. [cite_start]With over 181,000 possible configurations, my goal was to move past "brute-force" guessing and create an intelligent agent that finds the **most efficient** sequence of moves to reach the goal state[cite: 93, 99].

## Key Features
* [cite_start]**Hands-on Interaction**: You can play the puzzle manually to test your own logic or use the shuffle feature to randomize the board[cite: 110].
* [cite_start]**The "Brain" (A* Algorithm)**: I implemented the A* search algorithm, which uses the **Manhattan Distance heuristic** to guarantee the shortest path to a solution[cite: 94, 102].
* [cite_start]**Guided Solutions**: If you get stuck, the AI doesn’t just jump to the end—it visualizes each individual move so you can follow its logic step-by-step[cite: 95].

## Built With
* **Python**: The core language used for all logic and search functions.
* [cite_start]**Tkinter**: A standard Python library used to create a clean, responsive Graphical User Interface (GUI)[cite: 108, 110].
* **A* Search & Heuristics**: The mathematical foundations that ensure the solver is both fast and optimal[cite: 104, 106].

## How to Try It
1.  **Get the files**: Download or clone this repository to your computer.
2.  **Launch the app**: Open your terminal or command prompt and run:
    ```bash
    python main.py
    ```
3.  [cite_start]**Play & Shuffle**: Use the **Shuffle** button to scramble the tiles, or move them yourself by clicking on them[cite: 110].
4.  [cite_start]**Let the AI take over**: Click **Solve** to let the A* algorithm calculate the path[cite: 110].
5.  **Learn the steps**: Use the **Show steps** and **Next** buttons to watch the AI's "thought process" in action[cite: 110].

## Project Structure
* **`main.py`**: This is the heart of the user experience. [cite_start]It handles the buttons, the grid display, and the interaction logic[cite: 110].
* **`solver.py`**: This is the engine room. [cite_start]It contains the mathematical logic for the A* algorithm and the Manhattan Distance calculations[cite: 109].

## Why I Built This
I chose this problem because it is a perfect bridge between theory and practice[cite: 116]. It allowed me to take abstract concepts like "state-space search" and "heuristics" and turn them into something visual and interactive[cite: 118]. This project has deepened my understanding of how AI can be used to solve optimization problems effectively.

## Known Limitations & Future Goals
Currently, the solver is optimized for $3 \times 3$ grids, and very complex shuffles can sometimes cause the interface to pause while the AI "thinks"[cite: 114]. In the future, I plan to add:
* [cite_start]Smooth sliding animations for the tiles[cite: 120].
* [cite_start]Support for larger puzzles, such as $4 \times 4$ or $5 \times 5$ grids[cite: 120].
* A comparison tool to see how A* performs against other algorithms like BFS or DFS[cite: 120].
