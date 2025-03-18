from cell import Cell
import random
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed = None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed != None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)


    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            can_visit = []
            if i + 1 <= self._num_cols -1 and self._cells[i+1][j].visited == False:
                can_visit.append((i+1, j))
            if i - 1 >= 0 and self._cells[i-1][j].visited == False:
                can_visit.append((i-1, j))
            if j + 1 <= self._num_rows -1 and self._cells[i][j+1].visited == False:
                can_visit.append((i, j+1))
            if j - 1 >= 0 and self._cells[i][j-1].visited == False:
                can_visit.append((i, j-1))
            if len(can_visit) == 0:
                self._draw_cell(i, j)
                return
            p, q = can_visit[random.randrange(0, len(can_visit))]

            # Delete walls between current and next cell
            if p > i:  # moving right in the columns
                self._cells[i][j].has_right_wall = False  
                self._cells[p][q].has_left_wall = False   
            elif p < i:  # moving left in the columns
                self._cells[i][j].has_left_wall = False   
                self._cells[p][q].has_right_wall = False  
            elif q > j:  # moving down in the rows
                self._cells[i][j].has_bottom_wall = False 
                self._cells[p][q].has_top_wall = False    
            elif q < j:  # moving up in the rows
                self._cells[i][j].has_top_wall = False    
                self._cells[p][q].has_bottom_wall = False 

            self._draw_cell(i, j)
            self._break_walls_r(p, q)

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        # Check each direction
        can_visit = []
        if i + 1 <= self._num_cols -1 and self._cells[i+1][j].visited == False and self._cells[i][j].has_right_wall == False:
            can_visit.append((i+1, j))
        if i - 1 >= 0 and self._cells[i-1][j].visited == False and self._cells[i][j].has_left_wall == False:
            can_visit.append((i-1, j))
        if j + 1 <= self._num_rows -1 and self._cells[i][j+1].visited == False and self._cells[i][j].has_bottom_wall == False:
            can_visit.append((i, j+1))
        if j - 1 >= 0 and self._cells[i][j-1].visited == False and self._cells[i][j].has_top_wall == False:
            can_visit.append((i, j-1))


        for direction in can_visit:
            p, q = direction
            self._cells[i][j].draw_move(self._cells[p][q])
            if self._solve_r(p, q) == True:
                return True
            self._cells[i][j].draw_move(self._cells[p][q], undo=True)
        return False
        
        
        

    def solve(self):
        return self._solve_r(0, 0)


