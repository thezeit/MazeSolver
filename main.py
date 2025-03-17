from tkinter import Tk, BOTH, Canvas
from time import sleep

class Window(object):

    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root)
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):

        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line(object):

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="black", width=3):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=width
        )

class Cell(object):

    def __init__(
        self, top_left_x, top_left_y, bottom_right_x, bottom_right_y, _win
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.top_left_x = top_left_x
        self.bottom_right_x = bottom_right_x
        self.top_left_y = top_left_y
        self.bottom_right_y = bottom_right_y
        self._win =_win

    def draw(self):

        top_left = Point(self.top_left_x, self.top_left_y)
        top_right = Point(self.bottom_right_x, self.top_left_y)
        bottom_left = Point(self.top_left_x, self.bottom_right_y)
        bottom_right = Point(self.bottom_right_x, self.bottom_right_y)

        left_wall = Line(top_left, bottom_left)
        top_wall = Line(top_left, top_right)
        right_wall = Line(top_right, bottom_right)
        bottom_wall = Line(bottom_left, bottom_right)

        if self.has_left_wall:
            self._win.draw_line(left_wall, "black")
        if self.has_top_wall:
            self._win.draw_line(top_wall, "black")
        if self.has_right_wall:
            self._win.draw_line(right_wall, "black")
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, "black")
    
    def draw_move(self, destination_cell, undo=False):

        depart_x = int((self.top_left_x + self.bottom_right_x) / 2)
        depart_y = int((self.top_left_y + self.bottom_right_y) / 2)

        destination_x = int((destination_cell.top_left_x + destination_cell.bottom_right_x) / 2)
        destination_y = int((destination_cell.top_left_y + destination_cell.bottom_right_y) / 2)

        self.depart_point = Point(depart_x, depart_y)
        self.destination_point = Point(destination_x, destination_y)
        self.turn_point = Point(depart_x, destination_y)

        if undo == False:
            color = "red"
        else:
            color = "gray"

        self.departure_line = Line(self.depart_point, self.turn_point)
        self.destination_line = Line(self.turn_point, self.destination_point)

        # Actually draw the lines

        self._win.draw_line(self.departure_line, color)
        self._win.draw_line(self.destination_line, color)

    
class Maze(object):

    def __init__(self, x1, y1, cell_size_x, cell_size_y, win):

        self.x1 = x1
        self.y1 = y1
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.num_rows = int(self.win.width / cell_size_x)
        self.num_cols = int(self.win.height / cell_size_y)

    def _create_cells(self):

        top_left_x = self.x1
        top_left_y = self.x1
        bottom_right_x = self.x1 + self.cell_size_x
        bottom_right_y = self.y1 + self.cell_size_y

        cell_list = [[] for i in range(self.num_cols)]

        for row in cell_list:

            for i in range(self.num_cols):
                cell_list[i].append(Cell(top_left_x, top_left_y, bottom_right_x, bottom_right_y, self.win))
                top_left_x += self.cell_size_x
                bottom_right_x += self.cell_size_y

            top_left_y += self.cell_size_y
            top_left_x += self.cell_size_x

        self.cell_list = cell_list            



    def _draw_cell(self, i, j):
        pass

    def _animate(self):
        pass





def main():

    win = Window(800, 600)

    new_maze = Maze(0, 0, 50, 50, win)
    print("New Maze >>>>> \n", new_maze._create_cells())

    win.wait_for_close()



main()

"""    cell_one = Cell(0, 0, 100, 100, win)
    cell_one.draw()
    cell_two = Cell(100, 100, 200, 200, win)
    cell_two.draw()
        # Test for linking line
    cell_one.draw_move(cell_two, undo=True)"""