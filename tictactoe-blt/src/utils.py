# Helpers
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


from globals import *


def to_gamecoord(loc):
    x, y = loc
    return y // ratio_rows, x // ratio_cols


def to_corner(loc):
    x, y = loc
    xc = ratio_cols * (x // ratio_cols)
    yc = ratio_rows * (y // ratio_rows)
    return xc, yc
