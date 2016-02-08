import curses as crs
import view.logic as log
__author__ = 'Kellan Childers'


def add_title(window, title,  window_y=0, bold=True, underline=True, color_scheme=1):
    """Add a title centered on a line.

    :param window: the window to title
    :param title: the title to add
    :param window_y: the height of the title
    :param bold: whether or not to bold the title (default True)
    :type bold: Boolean
    :param underline: whether or not to underline the title (default True)
    :type underline: Boolean
    :param color_scheme: the scheme to use for coloring the title (default 1)
    :return: null
    """
    height, width = window.getmaxyx()
    title_x, _ = log.center((len(title), 1), (width, height))
    window.addstr(window_y, title_x, title,
                  (crs.A_BOLD if bold else 0) |
                  (crs.A_UNDERLINE if underline else 0) |
                  (crs.color_pair(color_scheme)))
    window.refresh()


def color_border(window, start, stop, color_scheme=1):
    """Create a border around a window in a certain color.

    :param window: the window to add a border to.
    :param start: the starting coordinate on the screen
    :param stop: the ending coordinate on the screen
    :param color_scheme: the color to paint the border (default 1)
    :return: null
    """
    group = [(y, x) for x, y in log.create_box(start, stop)]
    draw_group(window, group, color_scheme, ' ')


def color_hash(window, start, stop, color_scheme=1):
    """Create a hash in a window in a certain color.

    :param window: the window to add a border to.
    :param start: the starting coordinate on the screen
    :param stop: the ending coordinate on the screen
    :param color_scheme: the color to paint the border (default 1)
    :return: null
    """
    group = [(y, x) for x, y in log.create_hash(start, stop)]
    draw_group(window, group, color_scheme, ' ')


def draw_group(window, group, color_scheme=1, character=' '):
    """Draw a group of points.

    :param window: the window to draw on
    :param group: the list of points in form (y, x) to draw
    :param color_scheme: the number of the color scheme to use for coloring (default 1)
    :param character: the type of character to draw (default space)
    :type character: String
    :return: null
    """
    for point in group:
        try:
            window.addstr(point[0], point[1], character, crs.color_pair(color_scheme))
        except crs.error:
            # curses.error when point is not viewable and can safely be ignored.
            pass

    window.refresh()
