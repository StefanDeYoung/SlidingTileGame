import math
import pdb

class State:
    '''State represents a node on our search tree. It knows its state, parent, path from root, and can expand itself'''

    def __init__(self, state, parent, path, depth, cost):
        self.state  = state        # state is a tuple, eg. ('0','1','2',...,'n-1')
        self.parent = parent       # the state of the immediate predecessor state of this state
        self.path   = path         # cumulative path leading to this state, eg. a list ['Up', 'Right', 'Down'...]
        self.depth  = depth        # depth in search tree of this state; an integer
        self.cost   = cost         # cumulative cost of the path to reach this state from the initial state
        return

    def getSuccessors(self):
        '''Returns successor: a list of state objects'''

        actions = ["Up", "Down", "Left", "Right"]
        successors = []

        parent = self

        n        = int(math.sqrt(len(parent.state))) #size of board
        idx      = parent.state.index(0)    #get 1D index of 0 in parent state
        col, row = index1to2(idx, n)        #get 2D indices of 0 in parent state

        # Check each potential action to determine if it is possible. If the action
        # is possible, set validAction to True, and append the candidate child to the
        # list of successors
        for direction in actions:
            validAction = True  #Assume that it's true, and the if chain will determine if it's false

            child  = State(parent.state, parent.state, [], parent.depth + 1, parent.cost + 1)
            child_state_list = list(child.state) #Convert the state into a mutable list

            #pdb.set_trace()

            if (direction == 'Up' and row - 1 >= 0):
                child_state_list[idx], child_state_list[index2to1(row - 1, col, n)] = child_state_list[index2to1(row - 1, col, n)], child_state_list[idx]
            elif (direction == 'Down' and row + 1 < n):
                child_state_list[idx], child_state_list[index2to1(row + 1, col, n)] = child_state_list[index2to1(row + 1, col, n)], child_state_list[idx]
            elif (direction == 'Left' and col - 1 >= 0 ):
                child_state_list[idx], child_state_list[index2to1(row, col - 1, n)] = child_state_list[index2to1(row, col - 1, n)], child_state_list[idx]
            elif (direction == 'Right' and col + 1 < n):
                child_state_list[idx], child_state_list[index2to1(row, col + 1, n)] = child_state_list[index2to1(row, col + 1, n)], child_state_list[idx]
            else:
                validAction = False

            # if the action has been deemed valid, add the child to the list
            # of valid successors
            if validAction:
                child.state = tuple(child_state_list)
                child.path = list(parent.path) + [direction]
                successors.append(child)

        return successors

def index1to2(idx, n):
    '''Convert a 1d array index to col, row format'''
    col = int(idx % n)
    row = int(idx/n)

    return col, row

def index2to1(col, row, n):
    '''Convert col,row array indices to 1d array index'''
    return int(col*n + row)
