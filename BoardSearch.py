# BoardSearch.py
import heapq

class State:

    def __init__(self, state, parent, path, depth, cost):
        self.state    = state        # stateID is a tuple, eg. ('0','1','2',...,'n-1')
        self.parent   = parent       # immediate predecessor state of this state (a tuple like stateID)
        self.path     = path         # cumulative path leading to this state, eg. a list ['Up', 'Right', 'Down'...]
        self.depth    = depth        # depth in search tree of this state; an integer
        self.pathCost = cost         # cumulative cost of the path to reach this state from the initial state
        return

    def getSuccessors(parent):
        '''Returns successor state objects'''

        actions = ["Up", "Down", "Left", "Right"]
        successors = []
        childState = parent.state

        n = math.sqrt(len(parent.state))
        idx = parent.state.index(0) #get 1D index of 0 in parent state
        row, col = index1to2(idx, n)

        # Check each potential action to determine if it is possible. If the action
        # is possible, set validAction to True, and carry out the action on childList
        for dir in actions:
            validAction = False         # evaluated below; determines if a proposed action is possible

            if (dir == 'Up' && row - 1 >= 0):
                    validAction = True
                    childState[idx], childState[index2to1(col, row + 1, n)] = childState[index2to1(col, row + 1, n)], childState[idx]
            elif (dir == 'Down' && row + 1 >= n):
                    validAction = True
                    childState[idx], childState[index2to1(col, row + 1, n)] = childState[index2to1(col, row + 1, n)], childState[idx]
            elif (dir == 'Left' && col - 1 >= 0 ):
                    validAction = True
                    childState[idx], childState[index2to1(col - 1, row, n)] = childState[index2to1(col - 1, row, n)], childState[idx]
            elif (dir == 'Right' && col + 1):
                    validAction = True
                    childState[idx], childState[index2to1(col + 1, row, n)] = childState[index2to1(col + 1, row, n)], childState[idx]

            # if the action has been deemed valid, complete the creation of a successor State object
            if validAction:
                childPath = parent.path[:]          # get the cumulative path to this point
                childPath.append(dir)
                childDepth = parent.depth + 1
                childCost = parent.pathCost + 1
                successors.append(State(childState, parent.state, childPath, childDepth, childCost))

        return successors


"""
Utility functions
"""

def index1to2(idx, n):
    '''Convert a 1d array index to col, row format'''
    row = int(idx/n)
    col = int(idx % n)
    return row, col

def index2to1(row, col, n):
    '''Convert col,row array indices to 1d array index'''
    return col*n + row

def isGoal(current, goal):
    return current.state == goal.state

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
