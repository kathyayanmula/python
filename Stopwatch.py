import simplegui

a = 0
b = 0
c = 0
d = 0
message = '0:00.0'
win = 0
total = 0
game = '0/0'


# defining the start handler
def start():
    global a, b, c, d, message
    timer.start()
    d += 1
    if d > 9:
        c += 1
        d = 0
        if c > 9:
            b += 1
            c = 0
            if b > 5:
                a += 1
                b = 0
    message = str(a) + ':' + str(b) + str(c) + '.' + str(d)


# defining the stop handler
def stop():
    global total, win, game
    timer.stop()
    if a or b or c or d > 0:
        total += 1
    if (a > 0 or b > 0 or c > 0) and (d == 0):
        win += 1
    game = str(win) + '/' + str(total)


# defining the reset handler

def reset():
    global a, b, c, d, message, game, win, total
    a = 0
    b = 0
    c = 0
    d = 0
    total = 0
    win = 0
    message = '0:00.0'
    game = '0/0'


# defining the canvas handler
def draw(canvas):
    canvas.draw_text(message, [90, 115], 45, 'white', 'sans-serif')
    canvas.draw_text(game, [250, 30], 25, 'red', 'sans-serif')


# creating and registering frame and timer handlers
frame = simplegui.create_frame('Stopwatch', 300, 200)
timer = simplegui.create_timer(100, start)
frame.add_button('Start', start)
frame.add_button('Stop', stop)
frame.add_button('Reset', reset)
frame.set_draw_handler(draw)

frame.start()



