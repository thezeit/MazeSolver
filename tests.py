import unittest
from main import Maze, Window

class Tests(unittest.TestCase):

    

    def test_maze_create_cells(self):

        test_win = Window(500, 500)
        cell_size_x = 12
        cell_size_y = 10
        m1 = Maze(0, 0, cell_size_x, cell_size_y, test_win, 10)
        m1._create_cells()
        self.assertEqual(len(m1.cell_list), 40)
        self.assertEqual(len(m1.cell_list[0]), 48)

    def test_maze_create_cells_two(self):

        test_win_two = Window(100, 100)
        cell_size_x = 12
        cell_size_y = 10
        m2 = Maze(0, 0, cell_size_x, cell_size_y, test_win_two, 10)
        m2._create_cells()
        self.assertEqual(len(m2.cell_list), 6)
        self.assertEqual(len(m2.cell_list[0]), 8)



if __name__ == "__main__":
    unittest.main()