from tkinter import *
import random


WIDTH = 900
HEIGHT = 300

PAD_W = 10
PAD_H = 100

BALL_SPEED_UP = 1.05
BALL_MAX_SPEED = 40
BALL_RADIUS = 30

INITIAL_SPEED = 20
BALL_X_SPEED = INITIAL_SPEED
BALL_Y_SPEED = INITIAL_SPEED

PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

right_line_distance = WIDTH - PAD_W


def update_score(player):
    global PLAYER_1_SCORE, PLAYER_2_SCORE
    if player == "right":
        PLAYER_1_SCORE += 1
        w2.itemconfig(p_1_text, text=PLAYER_1_SCORE)
    else:
        PLAYER_2_SCORE += 1
        c.itemconfig(p_2_text, text=PLAYER_2_SCORE)


def spawn_ball():
    global BALL_X_SPEED
    c.coords(BALL, WIDTH / 2 - BALL_RADIUS / 2,
             HEIGHT / 2 - BALL_RADIUS / 2,
             WIDTH / 2 + BALL_RADIUS / 2,
             HEIGHT / 2 + BALL_RADIUS / 2)
    BALL_X_SPEED = -(BALL_X_SPEED * -INITIAL_SPEED) / abs(BALL_X_SPEED)



def bounce(action):
    global BALL_X_SPEED, BALL_Y_SPEED
    if action == "strike":
        BALL_Y_SPEED = random.randrange(-10, 10)
        if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
            BALL_X_SPEED *= -BALL_SPEED_UP
        else:
            BALL_X_SPEED = -BALL_X_SPEED
    else:
        BALL_Y_SPEED = -BALL_Y_SPEED


root = Tk()
root.title("Ping Pong")
win2 = Tk()
win2.title("win 3  ")
win3 = Tk()
win3.title("win 2")
w2 = Canvas(win2, width=300, height=HEIGHT, background="#003300")
w2.pack()
w3 = Canvas(win3, width=300, height=HEIGHT, background="#003300")
w3.pack()
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()


x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x-300, y))
win3.wm_geometry("+%d+%d" % (x, y))
win2.wm_geometry("+%d+%d" % (x+300, y))


BALL = c.create_oval(WIDTH / 2 - BALL_RADIUS / 2,
                     HEIGHT / 2 - BALL_RADIUS / 2,
                     WIDTH / 2 + BALL_RADIUS / 2,
                     HEIGHT / 2 + BALL_RADIUS / 2, fill="white")
LEFT_PAD = c.create_line(PAD_W / 2, 0, PAD_W / 2, PAD_H, width=10, fill="yellow")
RIGHT_PAD = c.create_line(WIDTH - PAD_W / 2, 0, WIDTH - PAD_W / 2,
                          PAD_H, width=PAD_W, fill="yellow")
p_1_text = w2.create_text(300 - 300 / 6, PAD_H / 4,
                         text=PLAYER_1_SCORE,
                         font="Arial 20",
                         fill="white")
p_2_text = c.create_text(WIDTH / 6, PAD_H / 4,
                         text=PLAYER_2_SCORE,
                         font="Arial 20",
                         fill="white")

BALL_X_CHANGE = 20
BALL_Y_CHANGE = 0
pad = w3.create_line(0,0,0,0,fill = "yellow")
ball_w2 = w2.create_oval(0,0,0,0,fill="black")
ball_w1 = w3.create_oval(0,0,0,0,fill="black")
def move_ball():
    global ball_left, ball_top,ball_right,ball_bot
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center = (ball_top + ball_bot) / 2

    if ball_right + BALL_X_SPEED < right_line_distance and \
            ball_left + BALL_X_SPEED > PAD_W:
        c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
    elif ball_right == right_line_distance or ball_left == PAD_W:
        if ball_right > WIDTH / 2:
            if c.coords(RIGHT_PAD)[1] < ball_center < c.coords(RIGHT_PAD)[3]:
                bounce("strike")
            else:
                update_score("left")
                spawn_ball()
        else:
            if c.coords(LEFT_PAD)[1] < ball_center < c.coords(LEFT_PAD)[3]:
                bounce("strike")
            else:
                update_score("right")
                spawn_ball()
    else:
        if ball_right > WIDTH / 2:
            c.move(BALL, right_line_distance - ball_right, BALL_Y_SPEED)
        else:
            c.move(BALL, -ball_left + PAD_W, BALL_Y_SPEED)
    if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
        bounce("ricochet")

def paint_ball():
    global ball_w2,ball_w1
    if ball_right <= 890 and ball_right >= 590:
        w2.delete(ball_w2)
        ball_w2 = w2.create_oval(ball_left-600,ball_top,ball_right-600 ,ball_bot,fill = "white")
        if ball_right - 600 <= 20 or ball_right - 600 >= 290:
            w2.delete(ball_w2)
    elif ball_right >= 310 and ball_right <= 590:
        w3.delete(ball_w1)
        ball_w1 = w3.create_oval(ball_left-300, ball_top, ball_right-300, ball_bot, fill="white")
        if ball_left - 300 <= 20 or ball_left - 300 >= 280 or ball_right - 300 >= 267:
            w3.delete(ball_w1)

def paint_pad():
    global pad
    w2.delete(pad)
    pad = w2.create_line(left-600,top,right-600,bot,width=10,fill = "yellow")

PAD_SPEED = 20
LEFT_PAD_SPEED = 0
RIGHT_PAD_SPEED = 0
def move_pads():
    global left,top,right,bot
    left,top,right,bot = c.coords(RIGHT_PAD)
    PADS = {LEFT_PAD: LEFT_PAD_SPEED,
            RIGHT_PAD: RIGHT_PAD_SPEED}
    for pad in PADS:
        c.move(pad, 0, PADS[pad])
        if c.coords(pad)[1] < 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])


def main():
    move_ball()
    move_pads()
    paint_ball()
    paint_pad()
    root.after(30, main)

c.focus_set()
w2.focus_set()


def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym == "w":
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "s":
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED = PAD_SPEED

c.bind("<KeyPress>", movement_handler)
w2.bind("<KeyPress>", movement_handler)

def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0


c.bind("<KeyRelease>", stop_pad)
w2.bind("<KeyRelease>", stop_pad)
main()
root.geometry("300x300")


root.mainloop()

