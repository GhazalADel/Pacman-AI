# Pacman AI Search Algorithms

**Course**: Fundamentals and Applications of Artificial Intelligence — Spring 1404  
**University**: Amirkabir University of Technology  

## Overview

Implementation of classic AI search algorithms to guide Pacman through mazes — eating all food and reaching the goal using uninformed and informed search.

## Implemented Algorithms

| Algorithm | Function |
|-----------|----------|
| Depth-First Search | `depthFirstSearch` |
| Breadth-First Search | `breadthFirstSearch` |
| Uniform Cost Search | `uniformCostSearch` |
| A* Search | `aStarSearch` |
| Iterative Deepening Search | IDS in `findPathToClosestDot` |

## Modified Files

- `search.py` — search algorithm implementations
- `searchAgents.py` — search agents, heuristics, and problem definitions
- `util.py` — data structures (stack, queue, priority queue)

## Running

```bash
# Play manually
python pacman.py

# Run with a search agent
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -z 0.5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

# Run autograder
python autograder.py
```

## Base Project

Based on the [UC Berkeley CS188 Pacman Project](http://ai.berkeley.edu/search.html).
