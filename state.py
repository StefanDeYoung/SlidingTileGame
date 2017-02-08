import math

class State:
    '''State represents a node on our search tree. It knows its state, parent, path from root, and can expand itself'''

    def __init__(self, state, parent, path, depth, cost):
        self.state    = state        # state is a list, eg. ('0','1','2',...,'n-1')
        self.parent   = parent       # immediate predecessor state of this state (a tuple like stateID)
        self.path     = path         # cumulative path leading to this state, eg. a list ['Up', 'Right', 'Down'...]
        self.depth    = depth        # depth in search tree of this state; an integer
        self.pathCost = cost         # cumulative cost of the path to reach this state from the initial state
        return

    def getSuccessors(self):
        '''Returns successor state objects'''

        actions = ["Up", "Down", "Left", "Right"]
        successors = []
        parent = self
        childState = parent.state

        n = int(math.sqrt(len(parent.state)))
        idx = parent.state.index(0) #get 1D index of 0 in parent state
        row, col = index1to2(idx, n)

        # Check each potential action to determine if it is possible. If the action
        # is possible, set validAction to True, and carry out the action on childList
        for dir in actions:
            validAction = False         # evaluated below; determines if a proposed action is possible

            if (dir == 'Up' and row - 1 >= 0):
                    validAction = True
                    childState[idx], childState[index2to1(col, row - 1, n)] = childState[index2to1(col, row - 1, n)], childState[idx]
            elif (dir == 'Down' and row + 1 < n):
                    validAction = True
                    childState[idx], childState[index2to1(col, row + 1, n)] = childState[index2to1(col, row + 1, n)], childState[idx]
            elif (dir == 'Left' and col - 1 >= 0 ):
                    validAction = True
                    childState[idx], childState[index2to1(col - 1, row, n)] = childState[index2to1(col - 1, row, n)], childState[idx]
            elif (dir == 'Right' and col + 1 < n):
                    validAction = True
                    childState[idx], childState[index2to1(col + 1, row, n)] = childState[index2to1(col + 1, row, n)], childState[idx]

            # if the action has been deemed valid, complete the creation of a successor State object
            if validAction:
                childPath = parent.path          # get the cumulative path to this point
                childPath.append(dir)
                childDepth = parent.depth + 1
                childCost = parent.pathCost + 1
                successors.append(State(childState, parent.state, childPath, childDepth, childCost))

        return successors

def index1to2(idx, n):
    '''Convert a 1d array index to col, row format'''
    row = int(idx/n)
    col = int(idx % n)
    return row, col

def index2to1(col, row, n):
    '''Convert col,row array indices to 1d array index'''
    return int(col*n + row)
