from graphics import Line, Point, Window


def main():
    win = Window(800, 600)
    line = Line(Point(50, 50), Point(400, 400))
    win.draw_line(line, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
