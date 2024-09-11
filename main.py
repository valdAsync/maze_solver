from graphics import Cell, Line, Point, Window


def main():
    win = Window(800, 600)
    line = Line(Point(50, 50), Point(400, 400))
    win.draw_line(line, "black")
    cell = Cell(50, 50, 400, 400, win)
    cell.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()
