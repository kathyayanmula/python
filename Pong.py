# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [50, 20]
ball_vel = [5, 5]
paddle1_pos = 200.0
paddle2_pos = 200.0
paddle1_vel = 0.0
paddle2_vel = 0.0
const_vel = 3.0
score1 = 0
score2 = 0


# helper function that spawns a ball by updating the
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    x = random.randrange(120, 240) // 60
    y = random.randrange(60, 180) // 60
    ball_vel = [x, y]
    if right == False:
        ball_vel[0] = - ball_vel[0]
        ball_vel[1] = - ball_vel[1]
    elif right == True:
        ball_vel[1] = -ball_vel[1]


# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    a = random.choice([True, False])
    ball_init(a)


def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] <= 20 or ball_pos[1] >= 380:
        ball_vel[1] = -ball_vel[1]
    if ((ball_pos[0] <= 28) and (ball_pos[1] <= int(paddle1_pos + 40) and ball_pos[1] >= int(paddle1_pos - 40))):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] = 1.1 * ball_vel[0]
        ball_vel[1] = 1.1 * ball_vel[1]
    elif ball_pos[0] <= 28:
        score2 += 1
        ball_init(True)

    if ((ball_pos[0] >= 572) and (ball_pos[1] <= int(paddle2_pos + 40) and ball_pos[1] >= int(paddle2_pos - 40))):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] = 1.3 * ball_vel[0]
        ball_vel[1] = 1.3 * ball_vel[1]
    elif ball_pos[0] >= 572:
        score1 += 1
        ball_init(False)

    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel) >= HALF_PAD_HEIGHT and (HEIGHT - (paddle1_pos + paddle1_vel)) >= HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if (paddle2_pos + paddle2_vel) >= HALF_PAD_HEIGHT and (HEIGHT - (paddle2_pos + paddle2_vel)) >= HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel

        # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_circle(ball_pos, 20, 5, 'white', 'white')

    # draw paddles
    c.draw_line([0, abs(paddle1_pos - HALF_PAD_HEIGHT)], [0, abs(paddle1_pos + HALF_PAD_HEIGHT)], 14, 'white')
    c.draw_line([600, abs(paddle2_pos - HALF_PAD_HEIGHT)], [600, abs(paddle2_pos + HALF_PAD_HEIGHT)], 14, 'white')

    # update ball

    # draw ball and scores
    c.draw_text('Score: ' + str(score1), [100, 50], 30, 'green')
    c.draw_text('Score: ' + str(score2), [450, 50], 30, 'green')


new_game()


def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= const_vel
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += const_vel
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= const_vel
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += const_vel


def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', new_game)

# start frame
frame.start()
