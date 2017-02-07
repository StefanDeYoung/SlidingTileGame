# BoardSearch.py
import heapq

class State:

    def __init__(self, state, action, parent, path, depth, cost):
        self.stateID = state        # stateID is a tuple, eg. ('0','1','2',...,'n-1')
        self.action = action        # action is one of 'Up', 'Down', 'Left', 'Right' 
        self.parentID = parent      # immediate predecessor state of this state (a tuple like stateID)
        self.path = path            # cumulative path leading to this state, eg. a list ['Up', 'Right', 'Down'...]
        self.depth = depth          # depth in search tree of this state; an integer
        self.pathCost = cost        # cumulative cost of the path to reach this state from the initial state
        return

class BoardSearchProblem:
    '''
    The BoardSearchProblem class is responsible for initializing a search problem,
    determining when the goal has been reached and generating successor (children)
    states to place on the fringe.
    '''
    def __init__(self, initialState, goalState, n):
        
        self.boardState = initialState
        self.goalState = goalState
        self.boardDim = n
        self.action = ''
        self.parent = ''
        self.path = []
        self.depth = 0
        self.pathCost = 0
        self.startState = State(self.boardState, self.action, self.parent, self.path, self.depth, self.pathCost)
        
        self.bfsActions = ['Up', 'Down', 'Left', 'Right']
        
        return

    def getStartState(self):
        return self.startState

    def isGoalState(self, state):
        isGoal = state.stateID == self.goalState
        return isGoal

    def getSuccessors(self, state):
        '''Returns successor (or child) states as a list of 4-tuples(childState, action, parent, path)'''

        # create an empty list to hold successor (child) nodes. The list will contain
        # complete State class objects, not just the stateID attribute.
        successors = []

        parentStateID = state.stateID   # this is a tuple
        
        # Convert parentStateID from tuple form (0,1,2,...,n-1) to list form eg. [0,1,2,...,n-1]
        parentList = list(parentStateID)
        
        # Find index of the "0" or blank tile
        z_Idx = parentStateID.index(0)
  
        # Check each potential action to determine if it is possible. If the action
        # is possible, set validAction to True, and carry out the action on childList
        for dir in self.bfsActions:
            validAction = False         # evaluated below; determines if a proposed action is possible 
            childList = parentList[:]   # create a copy of the parent
            
            if dir == 'Up':
                if z_Idx - self.boardDim >= 0:
                    validAction = True
                    # exchange the zero tile with the tile immediately above it
                    childList[z_Idx], childList[z_Idx-self.boardDim] = childList[z_Idx-self.boardDim], childList[z_Idx]
            elif dir == 'Down':
                if z_Idx + self.boardDim < len(parentList):
                    validAction = True
                    # exchange the zero tile with the tile immediately below it
                    childList[z_Idx], childList[z_Idx+self.boardDim] = childList[z_Idx+self.boardDim], childList[z_Idx]
            elif dir == 'Left':
                if (z_Idx % self.boardDim) - 1 >= 0:
                    validAction = True
                    # exchange the zero tile with the tile immediately to the left
                    childList[z_Idx], childList[z_Idx-1] = childList[z_Idx-1], childList[z_Idx]
            elif dir == 'Right':
                if (z_Idx % self.boardDim) + 1 < self.boardDim:
                    validAction = True
                    # exchange the zero tile with the tile immediately to the right
                    childList[z_Idx], childList[z_Idx+1] = childList[z_Idx+1], childList[z_Idx]

            # if the action has been deemed valid, complete the creation of a successor State object
            if validAction:
                childStateID = tuple(childList)
                childPath = state.path[:]          # get the cumulative path to this point
                childPath.append(dir)
                childDepth = state.depth + 1
                childCost = state.pathCost + 1
                successors.append(State(childStateID, dir, parentStateID, childPath, childDepth, childCost))

        return successors

"""
 Data structures for search
"""

class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0

class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def length(self):
        return len(self.list)
    
    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0

class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.

      Note that this PriorityQueue does not allow you to change the priority
      of an item.  However, you may insert the same item multiple times with
      different priorities.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        # FIXME: restored old behaviour to check against old results better
        # FIXED: restored to stable behaviour
        entry = (priority, self.count, item)
        # entry = (priority, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        #  (_, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

