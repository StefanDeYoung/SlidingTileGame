import sys
import math
import time
import BoardSearch as bs

def main(argv):
    '''
    Program is called from the command line like this:
            $ python driver.py <method> <boardLayout>
            where,
            <method> is one of bfs, dfs, ast, ida
            <boardLayout> is a comma separated list representing a nXn board
    '''
    #print ('Number of arguments: ', len(argv))
    #print ('Argument list: ', str(argv))

    searchType = argv[1]    # get search type requested (ie. bfs, dfs, ast, or ida)

    # change argv[2] from string '0,1,2,...,8' to a list ['0','1','2',...,'8'] then to a list of int [0,1,2,...,8]
    root = bs.State("", None, [], 0, 0)    #state, parent, path, depth, cost
    root.state = argv[2].split(',')
    root.state = [int(x) for x in root.state]

    # generate the goal state
    goal = bs.State(None, None, None, 0, 0)    #state, parent, path, depth, cost
    goal.state = range(int(math.sqrt(len(root.state))))

    # Call the solver and output the solution to a text file
    t_start = time.time()

    finish, pushes, pops, f_size, f_maxsize, expanded, maxDepth = solver (root, goal, searchType)

    t_end = time.time()

    ### Print output to file output.txt

    orig_stdout = sys.stdout
    f = open('output.txt', 'w')
    sys.stdout = f

    print ('path_to_goal: ',     node.path)
    print ('cost_of_path: ')
    print ('nodes_expanded: ',   expanded)
    print ('fringe_size: ',      f_size)
    print ('max_fringe_size: ',  f_maxsize)
    print ('search_depth: ',     node.depth)
    print ('max_search_depth: ', maxDepth)
    print ('running_time: ',     t_end - t_start)
    print ('max_ram_usage: ')

    sys.stdout = orig_stdout
    f.close()
    #End of printout

    # prepare to measure execution time of search function
    # t_Start = time.time()
    # finish, pushes, pops, f_size, f_maxsize, expanded, maxDepth = bfs(problem)
    # t_End = time.time()
    # print ('Reached goal:', finish.stateID, 'in time:', t_End-t_Start)
    # print ('Pushes:',pushes,', Pops:',pops,', Fringe @ goal:',f_size,', Fringe max size:',f_maxsize,', expanded:',expanded )
    # print ('Depth @ goal:', finish.depth, ', maxDepth:', maxDepth)

def solver(root, goal, searchType):

    if (searchType == 'bfs'):
        sol = bfs(root, goal)
        print(sol)
    elif (searchType == 'dfs'):
        sol = dfs(root, goal)
    elif (searchType == 'ast'):
        sol = ast(root, goal)
    elif (searchType == 'ida'):
        sol = ida(root, goal)
    else:
        print("Invalid searchType")

    return sol

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

def dfs(root, goal):
    print('dfs is not yet implemented')

def ast(root, goal):
    print('ast is not yet implemented')

def ida(root, goal):
    print('ida is not yet implemented')


# -------------------------------------------------------
''' This is where the program starts and retrieves the command line args'''
if __name__ == '__main__':  # python calls it's main program "__main__"
    main(sys.argv)          # sys.argv returns the command line string
# -------------------------------------------------------
