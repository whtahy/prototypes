# Copy/paste
# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


import gui


def test_title(s, x = 30, y = 10, w = 6, h = 2):
    title = ''
    for i in range(1, 8):
        title += str(i)
        gui.text(s, x, y - 1 + (h + 1) * (i - 1), color = 'black')
        gui.textbox('', x, y + (h + 1) * (i - 1), w, h, title = title)
