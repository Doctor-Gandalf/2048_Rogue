import math as mth
__author__ = 'Kellan Childers'
"""Functions which provide view functionality but don't interface with Curses."""


def bind_dimensions(current_width, current_height, max_width, max_height, ratio=7 / 8):
    """Limit the size of a window if the console is over a certain size.

    :param current_width: the width of the window
    :param current_height: the height of the window
    :param max_width: the minimum width to start binding the window
    :param max_height: the minimum height to start binding the window
    :param ratio: the ratio to limit the dimension by
    :return: the bound dimension
    """
    x = current_width if current_width <= max_width else floor(current_width * ratio)
    y = current_height if current_height <= max_height else floor(current_height * ratio)
    return x, y


def center(little_point, big_point):
    """Find point to start window on center.

    :param little_point: the smaller point
    :param big_point: the bigger point
    :return: the center of the dimensions
    """
    little_width, little_height = unpack(little_point)
    big_width, big_height = unpack(big_point)

    start_x = mth.floor((big_width - little_width) / 2)
    start_y = mth.floor((big_height - little_height) / 2)
    return start_x, start_y


def create_box(start, stop):
    """Make a hollow rectangle from two points.

    :param start: the starting coordinate of the box
    :param stop:  the end coordinate of the box
    :return: a group of points in (x, y) form that make the box
    """
    # Unpack arguments to keep things clear.
    start_x, start_y = unpack(start)
    stop_x, stop_y = unpack(stop, True)
    group = []

    # Add the four sides of the border one at a time for readability.
    group += [(x, start_y) for x in range(start_x, stop_x)]
    group += [(x, stop_y) for x in range(start_x, stop_x)]
    group += [(start_x, y) for y in range(start_y, stop_y)]
    group += [(stop_x, y) for y in range(start_y, stop_y+1)]

    return group


def create_hash(start, stop):
    """Make a four-lined hash from two points.

    :param start: the starting coordinate of the hash
    :param stop:  the end coordinate of the hash
    :return: a group of points in (x, y) form that make the hash
    """
    # Unpack arguments to keep things clear.
    start_x, start_y = unpack(start)
    stop_x, stop_y = unpack(stop, True)

    # The step in each direction is how far apart the hash lines are.
    x_step = mth.floor((stop_x - start_x)/4)+1
    y_step = mth.floor((stop_y - start_y)/4)+1
    group = []

    # Add the six lines of the hash one at a time for readability.
    group += [(x, start_y+y_step) for x in range(start_x, stop_x)]
    group += [(x, start_y+(2 * y_step)) for x in range(start_x, stop_x)]
    group += [(x, start_y+(3 * y_step)) for x in range(start_x, stop_x)]

    group += [(start_x+x_step, y) for y in range(start_y, stop_y)]
    group += [(start_x+(2*x_step), y) for y in range(start_y, stop_y)]
    group += [(start_x+(3*x_step), y) for y in range(start_y, stop_y)]

    return group


def unpack(point, is_end=False):
    """Unpack a point for easy assign-ability.

    :param point: the point to unpack
    :param is_end: subtract one if it is an endpoint (default False)
    :return: an unpacked point
    """
    x, y = point
    # Take away 1 from end points to account for starting at 0.
    x -= 1 if is_end else 0
    y -= 1 if is_end else 0

    return x, y
