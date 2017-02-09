import pdb

def bfs(root, goal):
    """Search the shallowest nodes in the search tree first."""

    max_depth = 0
    n_expanded = 0
    f_currentSize = 0
    f_maxsize = 0
    f_pops = 0
    f_pushes = 0

    visited_nodes = set()

    fringe = Queue()
    fringe.push(root)
    f_pushes += 1
    f_currentSize += 1

    pdb.set_trace()

    while not fringe.isEmpty():

        node = fringe.pop()
        f_pops += 1
        f_currentSize -= 1

        if isGoal(node, goal):
            return node, f_pushes, f_pops, f_currentSize, f_maxsize, n_expanded, max_depth

        if node.state not in visited_nodes:
            n_expanded +=1
            visited_nodes.add(node.state)
            successors = node.getSuccessors()

            for child_node in successors:
                if child_node.state not in visited_nodes:
                    fringe.push(child_node)

                    if child_node.depth > max_depth:
                        max_depth = child_node.depth

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
