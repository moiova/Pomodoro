from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
global_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():

    # stop the timer
    if global_timer is not None:
        win.after_cancel(global_timer)
        global reps
        reps = 0

        label_checkmark.config(text="")
        label_timer.config(text="Timer", fg=GREEN)

        canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        label_timer.config(text="Long break", fg=RED)
        label_checkmark.config(text="✔✔✔✔")
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_timer.config(text="Short break", fg=PINK)
        if reps == 2:
            label_checkmark.config(text="✔")
        elif reps == 4:
            label_checkmark.config(text="✔✔")
        elif reps == 6:
            label_checkmark.config(text="✔✔✔")
        count_down(short_break_sec)
    else:
        label_timer.config(text="Work session", fg=GREEN)

        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(timer):
    global global_timer
    minutes = math.floor(timer / 60)
    seconds = timer % 60

    if seconds <= 9:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if timer > 0:
        global_timer = win.after(1000, count_down, timer - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Pomodoro")
win.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="Timer", font=(FONT_NAME, 28), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

label_checkmark = Label(text="", fg=GREEN, bg=YELLOW, pady=10)
label_checkmark.grid(column=1, row=2)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)

win.mainloop()
