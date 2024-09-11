from tkinter import BOTH, Canvas, Tk


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.widget = Canvas(self.root, width=self.width, height=self.height)
        self.widget.pack()
        self.running = True

    def redraw(self):
        self.widget.update_idletasks()
        self.widget.update()

    def wait_for_close(self):
        if self.running:
            self.redraw()

    def close(self):
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)
