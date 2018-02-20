# Released under CC0:
# Summary: https://creativecommons.org/publicdomain/zero/1.0/
# Legal Code: https://creativecommons.org/publicdomain/zero/1.0/legalcode.txt

win_w, win_h = 1000, 600

rec_x = win_w * 0.9
rec_y = win_h / 2
rec_w = win_w * 0.01
rec_h = win_h * 0.2

r = 10
pos = PVector(win_w * 0.1, win_h / 2)
vel = PVector(6, 7)

def setup():
    frameRate(60)
    size(win_w, win_h)
    refresh()

def draw():
    global pos, vel, rec_y

    rec_y = mouseY - rec_h / 2
    refresh()

    pred = pos + vel
    step = PVector.copy(vel).normalize()

    if outside(pred):
        while inside(pos + step):
            pos.add(step)
        if outside_x(pos + step):
            vel.x = -vel.x
        if outside_y(pos + step):
            vel.y = -vel.y
    elif pred.dist(nearest(pred)) <= r:
        while pos.dist(nearest(pos)) > r + 1:
            pos.add(step)
        n = (pos - nearest(pos)).normalize()
        vel = vel - 2 * vel.dot(n) * n
    else:
        pos.add(vel)

def outside_x(pos):
    return not (r <= pos.x <= win_w - r)
def outside_y(pos):
    return not (r <= pos.y <= win_h - r)
def outside(pos):
    return outside_x(pos) or outside_y(pos)
def inside(pos):
    return not outside(pos)

def refresh():
    background(255)
    rect(rec_x, rec_y, rec_w, rec_h)
    ball()

def ball():
    ellipse(pos.x, pos.y, r*2, r*2)

def nearest(pos):
    near = PVector(pos.x, pos.y)
    rec_east = rec_x + rec_w
    rec_south = rec_y + rec_h

    if pos.x < rec_x:
        near.x = rec_x
    elif pos.x > rec_east:
        near.x = rec_east

    if pos.y < rec_y:
        near.y = rec_y
    elif pos.y > rec_south:
        near.y = rec_south

    return near
