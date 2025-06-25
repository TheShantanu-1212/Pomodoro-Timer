from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#48b362"
YELLOW = "#f7f5dd"
FONT_NAME = "JetBrainsMono"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
    Stops the countdown,
    resets the reps to 0,
    sets the timer counter to an empty string,
    deletes all the checkmarks and
    sets the timer label to display "Timer".
    """
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="")
    check_marks["text"] = ""
    timer_label["text"] = "Timer"


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Start the timer when the user presses the start button.
    """
    global reps
    reps += 1

    if reps % 2 != 0:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
        check_marks["text"] += "✔\n"
    else:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
        check_marks["text"] += "✔\n"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """
    Runs a countdown in the canvas
    text from count (seconds) to 0 (seconds).
    """
    global timer
    min_remaining = count // 60
    sec_remaining = count % 60
    canvas.itemconfig(timer_text, text=f"{min_remaining:02d}:{sec_remaining:02d}")

    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Creating the main window
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=3, bg=YELLOW)

# Creating a canvas for the tomato image and the timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="assets/tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(
    100, 130, text="", fill="white", font=(FONT_NAME, 30, "bold")
)
canvas.grid(row=1, column=1)

# Creating the timer label
timer_label = Label()
timer_label.config(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

# Creating the start button
start_button = Button(text="Start")
start_button.config(font=(FONT_NAME, 10), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Creating the reset button
reset_button = Button(text="Reset")
reset_button.config(font=(FONT_NAME, 10), highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Creating the cycle counter label
check_marks = Label(text="")
check_marks.config(font=(FONT_NAME, 25), fg=GREEN, bg=YELLOW, highlightthickness=0)
check_marks.grid(row=3, column=1)


window.mainloop()
