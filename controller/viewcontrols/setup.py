import curses
import view.boardview as brd
__author__ = 'Kellan Childers'


def init(stdscr):
    """Start up standard screen to allow easy setup for apps.

    :param stdscr: the standard screen used in curses
    :return: null
    """
    # Ensures a clean visual space.
    stdscr.clear()
    curses.curs_set(False)

    # Set the background of the app to the secondary color.
    stdscr.bkgd(' ', curses.color_pair(1))
    stdscr.refresh()


def draw_background(stdscr, title="2048 Rogue-Agile Edition", color_scheme=2):
    """Draw the background of the game on the screen.

    :param stdscr: the standard screen used in curses
    :param title: the title for the background (default "2048 Rogue-Agile Edition")
    :param color_scheme: the color scheme for the background (default 2)
    :return: null
    """
    console_height, console_width = stdscr.getmaxyx()
    brd.color_border(stdscr, (0, 0), (console_width, console_height), color_scheme)
    brd.color_hash(stdscr, (0, 0), (console_width, console_height), color_scheme)
    brd.add_title(stdscr, title, underline=False, color_scheme=color_scheme)


def do_commands(stdscr, function):
    running = True
    while running:
        key = stdscr.getkey()
        try:
            running = function(key)
        except KeyError:
            pass
