#!/usr/bin/python3
import os
import curses

import controller as control
import controller.keycontrols as kc
import controller.viewcontrols as vc
__author__ = 'Kellan Childers'


def app(stdscr):
    vc.colorcontroller.create_color_schemes()
    vc.setup.init(stdscr)
    vc.setup.do_commands(stdscr, kc.execute_command)

if __name__ == "__main__":
    os.chdir(control.settingloader.get_main_directory())

    curses.wrapper(app)
