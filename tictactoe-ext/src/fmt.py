# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt


def menu(lst, left = '[', right = ']', n_newlines = 1):
    return space(label(lst, left, right), n_newlines)


def label(lst, left = '[', right = ']'):
    for i, x in enumerate(lst):
        lst[i] = f'{left}{itoa(i)}{right}  {x}'
    return lst


def space(lst, n_newlines = 1):
    if len(lst) <= 1:
        return lst

    sp_list = [lst[0]]
    for x in lst[1:]:
        sp_list += [''] * n_newlines
        sp_list.append(x)

    return sp_list


def text_w(lst, even = True):
    w = max([len(x) for x in lst]) // 2 + 1
    return w + (w % 2 == 1) * even


def itoa(x):
    return chr(ord('a') + x)
