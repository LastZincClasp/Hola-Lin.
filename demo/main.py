import curses
import map
import obj

def main(stdscr):
    stdscr.clear()
    a = map.Room()
    stdscr.addstr(0, 0, str(a))
    stdscr.refresh()
    while True:
        c = stdscr.getch()
        if c == curses.KEY_UP and a[p.y - 1][p.x] not in block:
            a[p.y][p.x] = " . "
            p.y -= 1
            a[p.y][p.x] = p.s
        elif c == curses.KEY_DOWN and a[p.y + 1][p.x] not in block:
            a[p.y][p.x] = " . "
            p.y += 1
            a[p.y][p.x] = p.s
        elif c == curses.KEY_LEFT and a[p.y][p.x - 1] not in block:
            a[p.y][p.x] = " . "
            p.x -= 1
            a[p.y][p.x] = p.s
        elif c == curses.KEY_RIGHT and a[p.y][p.x + 1] not in block:
            a[p.y][p.x] = " . "
            p.x += 1
            a[p.y][p.x] = p.s
        elif c == ord(" ") and map.near(a, "Box", p):
            ttime += 1
            stdscr.addstr(12, 0, "You touch the box for {} time(s)".format(ttime))
        elif c == ord("q"):
            break

        stdscr.addstr(0, 0, str(a))
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
