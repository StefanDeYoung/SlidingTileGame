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
    print ('Number of arguments: ', len(argv))
    print ('Argument list: ', str(argv))

    searchType = argv[1]    # get search type requested (ie. bfs, dfs, ast, or ida)
    
    # change argv[2] from string '0,1,2,...,8' to a list ['0','1','2',...,'8']
    initState = argv[2].split(',')              # split the string into a list of single chars
    # convert list of strings ['0','1','2',...,'8'] to list of int [0,1,2,...,8]
    initState = [int(x) for x in initState]

    # Calculate board dimension (n X n)
    n = int(math.sqrt(len(initState)))

    # convert initState to a tuple (0,1,2,...,n-1)
    initState = tuple(initState)  

    # generate the goal state as a tuple --> (0,1,2,...,n-1) 
    goalState = tuple(range(len(initState)))
    
    print ('searchType: ', searchType)
    print ('initState: ', initState)
    print ('Goal State:', goalState)
    print ('Board dimension:', n)

    problem = bs.BoardSearchProblem(initState, goalState, n)

    # prepare to measure execution time of search function
    t_Start = time.time()
    finish, pushes, pops, f_size, f_maxsize, expanded, maxDepth = bfs(problem)
    t_End = time.time()

    print ('Reached goal:', finish.stateID, 'in time:', t_End-t_Start)
    print ('Pushes:',pushes,', Pops:',pops,', Fringe @ goal:',f_size,', Fringe max size:',f_maxsize,', expanded:',expanded )
    print ('Depth @ goal:', finish.depth, ', maxDepth:', maxDepth)

    ### Print output to file output.txt
    orig_stdout = sys.stdout
    f = open('output.txt', 'w')
    sys.stdout = f

    print ('path_to_goal:',finish.path)
    print ('cost_of_path:')
    print ('nodes_expanded:', expanded)
    print ('fringe_size:', f_size)
    print ('max_fringe_size:', f_maxsize)
    print ('search_depth:', finish.depth)
    print ('max_search_depth:', maxDepth)
    print ('running_time:')
    print ('max_ram_usage:')   

    sys.stdout = orig_stdout
    f.close()
    #End of printout 
    
def bfs(problem):
    """Search the shallowest nodes in the search tree first."""

    startNode = problem.getStartState()
    print ('** B F S   **************************************')
    #print ('StartNode.state:(', startNode.stateID,'), Parent:(',startNode.parentID,'), Path:(',startNode.path,')')
    #print ('Goal:', problem.goalState)

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
    y.push(startNode)
    f_pushes += 1
    f_currentSize += 1

    while not y.isEmpty():
        node = y.pop()
        f_pops += 1
        f_currentSize -= 1
        if problem.isGoalState(node):
            return node, f_pushes, f_pops, f_currentSize, f_maxsize, n_expanded, maxDepth
        if node.stateID not in visitedNodes:
            n_expanded +=1
            visitedNodes.add(node.stateID)
            for childNode in problem.getSuccessors(node):
                if childNode.stateID not in visitedNodes:
                    y.push(childNode)
                    if childNode.depth > maxDepth:
                        maxDepth = childNode.depth
                    f_pushes += 1
                    f_currentSize += 1
                    if f_currentSize > f_maxsize:
                        f_maxsize = f_currentSize
        #else:
            #print ('%%%%% node: ', node.stateID, ' alredy in "visited"')                

# -------------------------------------------------------
''' This is where the program starts and retrieves the command line args'''
if __name__ == '__main__':  # python calls it's main program "__main__"
    main(sys.argv)          # sys.argv returns the command line string
# -------------------------------------------------------
    
