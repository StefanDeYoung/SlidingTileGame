import sys, math, time      #builtin libraries
from state import State     #a Class for the nodes in our search tree
from Search_Types.bfs import bfs         #Breadth-first search solver
from Search_Types.dfs import dfs         #Depth-first search solver
from Search_Types.ast import ast         #A* search solver
from Search_Types.ida import ida         #??? search solver


def main(argv):
    '''
    Program is called from the command line like this:
            $ python driver.py <method> <boardLayout>
                <method> is one of bfs, dfs, ast, ida
                <boardLayout> is a comma separated list representing a nXn board
    '''

    ############################################################
    ###Get cmd line arguments, and create root and goal nodes
    ############################################################
    searchType = argv[1]    # get search type requested (ie. bfs, dfs, ast, or ida)

    ###Create root node with node.state as a tuple
    root       = State(None, None, [], 0, 0)    #state, parent, path, depth, cost
    root.state = argv[2].split(',')
    root.state = tuple([int(x) for x in root.state])

    ### Create goal node object with correct state as a tuple
    goal = State([], None, [], None, None)    #state, parent, path, depth, cost
    goal.state = tuple(range(int(math.sqrt(len(root.state)))))

    ###########################################
    ### Call the solver and time its operation
    ###########################################
    t_start = time.time()

    if (searchType == 'bfs'):
        finish, pushes, pops, f_size, f_maxsize, expanded, maxDepth = bfs(root, goal)
    elif (searchType == 'dfs'):
        finish, pushes, pops, f_size, f_maxsize, expanded, maxDepth = dfs(root, goal)
    elif (searchType == 'ast'):
        finish, pushes, pops, f_size, f_maxsize, expanded, maxDepth = ast(root, goal)
    elif (searchType == 'ida'):
        finish, pushes, pops, f_size, f_maxsize, expanded, maxDepth = ida(root, goal)
    else:
        print("Invalid searchType")

    t_end = time.time()

    ####################################
    ### Print output to file output.txt
    ####################################
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

#
# Call the main function
# -------------------------------------------------------
'''This is where the program starts'''
if __name__ == '__main__':  # python calls it's main program "__main__"
    main(sys.argv)          # sys.argv returns the command line string
# -------------------------------------------------------
