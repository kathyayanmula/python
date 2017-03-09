# computer chooses a number between one and hundred
# and you have to guess it using the binary search
# an inpu to guess the number and the computer returns if it
# is higher or lower than the number
# if guessed right the game ends you will have only 7 guesses

# importing the modules
import simplegui
import random

# declaring global variables
x = 0
guess = 7
a = ''
b = ''
y = random.randint(0, 100)


# defining input handler
def inp(t):
    global x, guess, a, b
    x = float(t)
    guess -= 1

    if guess >= 0:
        if y > x:
            a = 'The number is greater than ' + str(x)
            b = 'Number of guesses left ' + str(guess)
        elif y < x:
            a = 'The number is less than ' + str(x)
            b = 'Number of guesses left ' + str(guess)
        else:
            a = 'Bingo! You guessed it right'
            b = ''
    else:
        b = 'No more guesses left'

        # defining button handlers


def reset():
    global a, b, x, y, guess
    x = 0
    y = random.randint(1, 100)
    guess = 8
    inp(x)
    a = ' Input a number'


def range():
    global y, guess
    y = random.randint(1, 1000)
    guess = 11


# defining canvas event handler
def draw(canvas):
    canvas.draw_text(a, [50, 60], 26, 'red')
    canvas.draw_text(b, [50, 90], 26, 'red')


# registering the handlers
frame = simplegui.create_frame('Guess', 400, 400)
frame.add_input('input', inp, 30)
frame.set_draw_handler(draw)
frame.add_button('Reset', reset, 100)
frame.add_button('1 to 1000', range, 100)

# starting frame
frame.start()