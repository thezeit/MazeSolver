import unittest
import random

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_reset_cells_visited(self):
        # Create a maze
        maze = Maze(0, 0, 14, 14, 10, 10)
        
        # Set some cells' visited to True
        maze._cells[0][0].visited = True
        maze._cells[1][1].visited = True
        
        # Call the reset method
        maze._reset_cells_visited()
        
        # Verify all cells have visited = False
        for column in maze._cells:
            for cell in column:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
