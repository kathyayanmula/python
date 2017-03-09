# implementation of card game - Memory

import simplegui
import random

a = list(range(8))
b = list(range(8))
card_list = []

exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
           False]
card_list = a + b

random.shuffle(card_list)


# helper function to initialize globals
def init():
    global state, moves, card_pos
    card_pos = []
    random.shuffle(card_list)
    state = 0
    moves = 0
    label.set_text('Moves = 0')
    for i in range(16):
        exposed[i] = False


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, moves, card_pos

    i = pos[0] // 50

    if not exposed[i]:
        exposed[i] = True
        card_pos.append(i)

        if state == 0:
            state = 1
            moves += 1

        elif state == 1:
            state = 2

        else:
            if card_list[card_pos[-2]] != card_list[card_pos[-3]]:
                exposed[card_pos[-2]] = False
                exposed[card_pos[-3]] = False
            state = 1
            moves += 1
    label.set_text('Moves = ' + str(moves))


# cards are logically 50x100 pixels in size
def draw(canvas):
    for i in range(16):
        if exposed[i]:
            canvas.draw_text(str(card_list[i]), [50 * i, 70], 70, 'White', 'sans-serif')
        if not exposed[i]:
            canvas.draw_polygon([[50 * i, 0], [50 * (i + 1), 0], [50 * (i + 1), 100], [50 * i, 100]], 1, 'black',
                                'green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


