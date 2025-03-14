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

point_alpha = Point(10, 10)
point_beta = Point(100, 100)
line_inst_one = Line(point_alpha, point_beta)


def main():
    win = Window(800, 600)
    win.draw_line(line_inst_one)
    win.wait_for_close()


main()

