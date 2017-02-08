def bfs(root, goal):
    """Search the shallowest nodes in the search tree first."""

    '''
    for node in problem.getSuccessors(startNode):
        print ('bfs=>child:', node.stateID, ', action:', node.action, ', parent:', node.parentID, ', path:', node.path)
    '''
    maxDepth = 0
    n_expanded = 0
    f_currentSize = 0
    f_maxsize = 0
    f_pops = 0
    f_pushes = 0

    y = bs.Queue()
    visitedNodes = set()
    y.push(root)
    f_pushes += 1
    f_currentSize += 1

    while not y.isEmpty():
        node = y.pop()
        f_pops += 1
        f_currentSize -= 1
        if bs.isGoal(node, goal):
            return node, f_pushes, f_pops, f_currentSize, f_maxsize, n_expanded, maxDepth
        if tuple(node.state) not in visitedNodes:
            n_expanded +=1
            visitedNodes.add(tuple(node.state))
            successors = node.getSuccessors()
            for childNode in successors:
                if tuple(childNode.state) not in visitedNodes:
                    y.push(childNode)
                    if childNode.depth > maxDepth:
                        maxDepth = childNode.depth
                    f_pushes += 1
                    f_currentSize += 1
                    if f_currentSize > f_maxsize:
                        f_maxsize = f_currentSize

    return "We did not return a solution for some reason"

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

def isGoal(current, goal):
    return current.state == goal.state
