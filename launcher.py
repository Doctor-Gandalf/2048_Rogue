#!/usr/bin/python3
import os
import curses as crs

import model.plots as pl

import view.boardview as brd

import controller.settingloader as sl
import controller.keycontrols as kc
import controller.viewcontrols as vc
__author__ = 'Kellan Childers'


def app(stdscr):
    vc.create_color_schemes()
    vc.init(stdscr)

    brd.color_border(stdscr, (0, 0), stdscr.getmaxyx(), 3)

    board = pl.Plot(4, 4)
    for x in range(4):
        for y in range(4):
            board[x][y] = pl.Tile(2, str(2))
    board[0][0] += pl.Tile(2, str(2))

    stdscr.addstr(0, 0, str(board))
    stdscr.refresh()

    vc.setup.do_commands(stdscr, kc.execute_command)

if __name__ == "__main__":
    os.chdir(sl.get_main_directory())

    crs.wrapper(app)
