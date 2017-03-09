import simplegui

ball_pos = [50, 60]
a = [300, 390]
b = [335, 390]
vel = [0, 0]
c = 3
d = 2


def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        vel[0] -= d
        vel[1] -= d
    elif key == simplegui.KEY_MAP['right']:
        vel[1] += d
        vel[0] += d


def keyup(key):
    vel[0] = 0
    vel[1] = 0


def draw(canvas):
    global c
    a[0] += vel[0]
    b[0] += vel[1]
    ball_pos[0] += c
    ball_pos[1] += c
    if ball_pos[0] < 20 or ball_pos[0] > 580:
        c = -c
    elif ball_pos[1] < 20:
        c = -c
    elif ball_pos[1] == 360 and (ball_pos[0] >= a[0] or ball_pos[0] <= b[0]):
        c = -c

    canvas.draw_circle(ball_pos, 20, 5, 'red', 'white')
    canvas.draw_line(a, b, 20, 'gray')


frame = simplegui.create_frame('velocity control', 600, 400)

frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

frame.start()