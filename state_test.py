import unittest
import pdb
import math
from state import *

class StateTestCase(unittest.TestCase):
    '''Tests for the State class'''

    def test_can_init_state(self):
        #Can we initialize a state?
         node = State((), None, [], 0, 0)
         self.assertTrue(isinstance(node, State))

    def test_can_get_member_variables(self):
        node = State((1,2,3,4,0,5,6,7,8), (1,2,3,0,4,5,6,7,8), ["Right"], 1, 1)

        self.assertTrue(node.state == (1,2,3,4,0,5,6,7,8))
        self.assertTrue(node.parent == (1,2,3,0,4,5,6,7,8))
        self.assertTrue(node.path == ["Right"])
        self.assertTrue(node.depth == 1)
        self.assertTrue(node.cost == 1)

    def test_can_calculate_n_2x2(self):
        #Can we calculate n for a 2x2 grid?
        node = State((0,1,2,3), None, [], 0, 0)
        n = int(math.sqrt(len(node.state)))
        self.assertTrue(n==2)

    def test_can_calculate_n_3x3(self):
        #Can we calculate n for a 2x2 grid?
        node = State((0,1,2,3,4,5,6,7,8), None, [], 0, 0)
        n = int(math.sqrt(len(node.state)))
        self.assertTrue(n==3)

    def test_can_find_0_index(self):
        node = State((1,2,3,0,4,5,6,7,8), None, [], 0, 0)
        idx = node.state.index(0)
        self.assertTrue(idx==3)

    def test_can_get_2d_index_from_1d(self):
        node = State((1,2,3,0,4,5,6,7,8), None, [], 0, 0)
        n = int(math.sqrt(len(node.state)))
        idx = node.state.index(0)
        col, row = index1to2(idx, n)
        self.assertTrue(col == 0 and row == 1)

    def test_can_get_1d_index_from_2d(self):
        indices = []
        n = 3

        for row in range(n):
            for col in range(n):
                indices.extend([index2to1(row,col,n)]) #Add index to list

        for i in range(n*n):
            self.assertTrue(indices[i]==i)

    def test_can_get_index_Up_one_row(self):
        n = 3
        row, col = 1,1

        up_one_row = index2to1(row-1,col,n)
        self.assertTrue(up_one_row == 1)

    def test_successors_is_a_list(self):
        node = State((1,2,3,4,0,5,6,7,8), None, [], 0, 0)
        successors = node.getSuccessors()
        self.assertTrue(isinstance(successors, list))

    def test_4_successors_for_middle_of_3x3(self):
        node = State((1,2,3,4,0,5,6,7,8), None, [], 0, 0)
        successors = node.getSuccessors()
        self.assertTrue(len(successors) == 4)

    def test_items_in_successors_are_States(self):
        node = State((1,2,3,4,0,5,6,7,8), None, [], 0, 0)
        successors = node.getSuccessors()

        for item in successors:
            self.assertTrue(isinstance(item, State))

    def test_successors_have_good_path_direction(self):
        node = State((1,2,3,4,0,5,6,7,8), None, [], 0, 0)
        successors = node.getSuccessors()
        actions = ["Up","Down", "Left", "Right"]

        for i in range(len(successors)):
            #pdb.set_trace()
            self.assertTrue(successors[i].path == [actions[i]])

    def test_successors_have_good_flips(self):
        node = State((1,2,3,4,0,5,6,7,8), None, [], 0, 0)
        successors = node.getSuccessors()

        self.assertTrue(successors[0].state == (1,0,3,4,2,5,6,7,8))  #Up
        self.assertTrue(successors[1].state == (1,2,3,4,7,5,6,0,8))  #Down
        self.assertTrue(successors[2].state == (1,2,3,0,4,5,6,7,8))  #Left
        self.assertTrue(successors[3].state == (1,2,3,4,5,0,6,7,8))  #Right

if __name__ == '__main__':
    unittest.main()
