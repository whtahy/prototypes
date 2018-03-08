# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import math

import fmt
from config import *


#
# Widget #######################################################################

# TODO: menu widget

def textbox(
        lst,
        x = None,
        y = None,
        w = None,
        h = None,
        perc_x = 50,
        perc_y = 50,
        title = None,
        padding = 4,
        border = True,
        color_title = 'cyan',
        color_text = 'white',
        color_bk = 'black',
        color_border = 'white'):
    if w is None:
        w = 2 * padding + fmt.text_w(lst)

    if h is None:
        h = 2 * padding + len(lst)

    if x is None:
        x = offset(w, win_w, perc = perc_x)

    if y is None:
        y = offset(h, win_h, perc = perc_y)

    # background
    blt.color(color_bk)
    fill(x, y, w, h)

    # border
    if border:
        blt.layer(blt.state(blt.TK_LAYER) + 1)
        blt.color(color_border)
        box(x, y, w, h)

    # text
    blt.layer(blt.state(blt.TK_LAYER) + 1)
    blt.color(color_text)
    text_col(lst, x + padding, y + padding)

    # title
    if title:
        indent = offset(len(title) * font_x, w * cell_x - font_x) - 1

        blt.color(color_bk)
        highlight(x, y, len(title), indent)

        blt.color(color_title)
        text(title, x, y, indent)

    return x, y, w, h, padding


#
# Raw ##########################################################################

def box(
        x, y, w, h):
    y_h = y + h - 1
    x_w = x + w - 1
    w_inner = w - 2
    h_inner = h - 2

    blt.put(x, y, ch_nw)
    line_x(x + 1, y, w_inner)
    blt.put(x_w, y, ch_ne)

    line_y(x, y + 1, h_inner)
    line_y(x_w, y + 1, h_inner)

    blt.put(x, y_h, ch_sw)
    line_x(x + 1, y_h, w_inner)
    blt.put(x_w, y_h, ch_se)


def fill(
        x, y, w, h):
    for i in range(y, y + h):
        blt.printf(x, i, ch_box * w)


def highlight(
        x, y, w,
        offset_x = 0,
        offset_y = 0):
    text([ch_box] * w, x, y, offset_x, offset_y)


def line_x(
        x, y, length):
    for i in range(length):
        blt.put(x + i, y, ch_line_x)


def line_y(
        x, y, length):
    for i in range(length):
        blt.put(x, y + i, ch_line_y)


def text(
        lst, x, y,
        offset_x = 0,
        offset_y = 0):
    for i, ch in enumerate(lst):
        if ch in ('[', ']'):
            ch *= 2
        prefix = f'[offset={offset_x + i * (cell_x - font_x)},{offset_y}]'
        blt.printf(x, y, f'{prefix}{ch}')


def text_col(
        lst, x, y,
        offset_x = 0,
        offset_y = 0):
    for i, row in enumerate(lst):
        text(row, x, y + i, offset_x, offset_y)


#
# Helper #######################################################################

def corner(w, h, perc_w = 50, perc_h = 50):
    return offset(w, win_w, perc_w), offset(h, win_h, perc_h)


def offset(length, edge, perc = 50):
    return int(math.floor((edge - length) * perc / 100))
