# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import Stack, Queue, PriorityQueue
from game import Directions
from typing import List


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    fringe = Stack()
    closed = set()

    start = problem.getStartState()
    fringe.push((start, []))

    while True:
        if fringe.isEmpty():
            return []

        state, so_far_actions = fringe.pop()

        if problem.isGoalState(state):
            return so_far_actions

        if state not in closed:
            closed.add(state)

            for successor, action, _ in problem.getSuccessors(state):
                new_actions = so_far_actions + [action]
                fringe.push((successor, new_actions))


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = Queue()
    closed = set()

    start = problem.getStartState()
    fringe.push((start, []))

    while True:
        if fringe.isEmpty():
            return []

        state, so_far_actions = fringe.pop()

        if problem.isGoalState(state):
            return so_far_actions

        if state not in closed:
            closed.add(state)

            for successor, action, _ in problem.getSuccessors(state):
                new_actions = so_far_actions + [action]
                fringe.push((successor, new_actions))

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = PriorityQueue()
    closed = set()

    start = problem.getStartState()
    fringe.push((start, [], 0), 0)

    while True:
        if fringe.isEmpty():
            return []

        state, so_far_actions, so_far_costs = fringe.pop()

        if problem.isGoalState(state):
            return so_far_actions

        if state not in closed:
            closed.add(state)

            for successor, action, action_cost in problem.getSuccessors(state):
                new_actions = so_far_actions + [action]
                new_cost = so_far_costs + action_cost
                fringe.push((successor, new_actions, new_cost), new_cost)

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = PriorityQueue()
    closed = set()

    start = problem.getStartState()
    fringe.push((start, [], 0), 0 + heuristic(start, problem))

    while True:
        if fringe.isEmpty():
            return []

        state, so_far_actions, so_far_costs = fringe.pop()

        if problem.isGoalState(state):
            return so_far_actions

        if state not in closed:
            closed.add(state)

            for successor, action, action_cost in problem.getSuccessors(state):
                new_actions = so_far_actions + [action]
                g = so_far_costs + action_cost
                f = g + heuristic(successor, problem)
                fringe.push((successor, new_actions, g), f)


def iterativeDeepeningSearch(problem: SearchProblem) -> List[Directions]:
    initial_limit = 1

    while initial_limit <= 100:
        fringe = Stack()
        closed = set()

        fringe.push((problem.getStartState(), [], 0))

        while not fringe.isEmpty():
            state, so_far_actions, depth = fringe.pop()

            if problem.isGoalState(state):
                return so_far_actions

            if depth >= initial_limit:
                continue

            if state not in closed:
                closed.add(state)

                for successor, action, _ in problem.getSuccessors(state):
                    new_actions = so_far_actions + [action]
                    fringe.push((successor, new_actions, depth + 1))

        initial_limit += 1

    return []





# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
