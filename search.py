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


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    "*** YOUR CODE HERE ***"
    # print "Start:", problem.getStartState()
    # a, b = problem.getStartState()
    # print a
    # print b
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    movements = util.Stack()
    Visited = []
    movements.push((problem.getStartState(), []))
    Visited.append(problem.getStartState())
    # a, b = movements.pop()
    # print problem.getSuccessors(a)
    j = 0
    while movements.isEmpty() == 0:
        j = j + 1
        current_state, actions = movements.pop()
        for i in problem.getSuccessors(current_state):
            temp_state, n_direction = i[0], i[1]
            if j==1:
                print actions
            if temp_state not in Visited:
                if problem.isGoalState(temp_state):
                    return actions + [n_direction]
                else:
                    # print actions
                    movements.push((temp_state, actions + [n_direction]))
                    Visited.append(temp_state)

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    movements = util.Queue()
    Visited = []
    movements.push((problem.getStartState(), []))
    Visited.append(problem.getStartState())
    # a, b = movements.pop()
    # print problem.getSuccessors(a)
    j = 0
    while movements.isEmpty() == 0:
        j = j + 1
        current_state, actions = movements.pop()
        for i in problem.getSuccessors(current_state):
            temp_state, n_direction = i[0], i[1]
            if j==1:
                print actions
            if temp_state not in Visited:
                if problem.isGoalState(temp_state):
                    return actions + [n_direction]
                else:
                    # print actions
                    movements.push((temp_state, actions + [n_direction]))
                    Visited.append(temp_state)

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import Queue,PriorityQueue
    movements = PriorityQueue()                    
    movements.push(problem.getStartState(),0)
    path=[]                                      
    visited = []                                 
    temp_path=[]                                 
    main_path=PriorityQueue()
    current_state = movements.pop()
    while not problem.isGoalState(current_state):
        if current_state not in visited:
            visited.append(current_state)
            successors = problem.getSuccessors(current_state)
            for child,direction,cost in successors:
                temp_path = path + [direction]
                cost = problem.getCostOfActions(temp_path)
                if child not in visited:
                    movements.push(child, cost)
                    main_path.push(temp_path, cost)
        current_state = movements.pop()
        path = main_path.pop()    
    return path

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import Queue,PriorityQueue
    movements = PriorityQueue()                    
    movements.push(problem.getStartState(),0)
    path=[]                                      
    visited = []                                 
    temp_path=[]                                 
    main_path=PriorityQueue()
    current_state = movements.pop()
    while not problem.isGoalState(current_state):
        if current_state not in visited:
            visited.append(current_state)
            successors = problem.getSuccessors(current_state)
            for successor,way,cost in successors:
                temp_path = path + [way]
                cost = problem.getCostOfActions(temp_path) + heuristic(successor, problem)
                if successor not in visited:
                    movements.push(successor, cost)
                    main_path.push(temp_path, cost)
        current_state = movements.pop()
        path = main_path.pop()    
    return path

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
