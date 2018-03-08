# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt

from bearlibterminal import terminal as blt

#
# misc #########################################################################

frame_delay = 1

#
# game #########################################################################

board_cols = 3
board_rows = 3

#
# string #######################################################################

s_exit_game = 'Exit'
s_load = 'Load'
s_menu_main = 'Main Menu'
s_menu_pause = 'Game Paused'
s_new_game = 'New Game'
s_resume = 'Resume'
s_save = 'Save'
s_start = 'Start'

#
# keybinds #####################################################################

m_click = (blt.TK_MOUSE_LEFT,)
m_move = (blt.TK_MOUSE_MOVE,)

k_shift = blt.TK_SHIFT
k_ctrl = blt.TK_CONTROL

k_exit = (blt.TK_CLOSE,)
k_enter = (blt.TK_ENTER, blt.TK_KP_ENTER,)
k_esc = (blt.TK_ESCAPE,)

k_sw = (blt.TK_KP_1,)
k_s = (blt.TK_KP_2, blt.TK_DOWN,)
k_se = (blt.TK_KP_3,)
k_w = (blt.TK_KP_4, blt.TK_LEFT,)
k_center = (blt.TK_KP_5,)
k_e = (blt.TK_KP_6, blt.TK_RIGHT,)
k_nw = (blt.TK_KP_7,)
k_n = (blt.TK_KP_8, blt.TK_UP,)
k_ne = (blt.TK_KP_9,)

#
# char #########################################################################

ch_box = '[0x2588]'

ch_line_x = 0x2500
ch_line_y = 0x2502
ch_nw = 0x250c
ch_ne = 0x2510
ch_sw = 0x2514
ch_se = 0x2518

ch_square = 0xE000
ch_x = 0xE001
ch_o = 0xE002
ch_select = 0xE003
ch_victory = 0xE004

#
# layer ########################################################################

layer_board = 10
layer_menu = 50

#
# screen #######################################################################

screen_x = 1680
screen_y = 1050

cell_x = 16
cell_y = 16

win_multi = 0.8
win_w = round(screen_x * win_multi / cell_x)
win_h = round(screen_y * win_multi / cell_y)

#
# assets #######################################################################

square_x = 256
square_y = 256
square_w = square_x // cell_x
square_h = square_y // cell_y
board_w = board_cols * square_w
board_h = board_rows * square_h

#
# font #########################################################################

font_x = 8
font_y = 16
font_margin_n = 3
font_margin_s = 0

#
# folders ######################################################################

dir_assets = '../assets/'
save_path = '../save/save_game'
