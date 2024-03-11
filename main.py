from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError as error_msg:
    print(error_msg)
    df = pandas.read_csv("data/french_words.csv")

french_dic = df.to_dict(orient="records")
current_card = {}

def pick_random():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_dic)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card, image=front_img)
    flip_timer = window.after(3000, timer_card)

def save_progres():
    french_dic.remove(current_card)
    words_to_learn = pandas.DataFrame(french_dic)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    pick_random()

def timer_card():
    global current_card
    # txt = canvas.itemcget(card_word, "text")
    answer = current_card["English"]
    canvas.itemconfig(card, image=back_img)
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=answer)


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, timer_card)

canvas = Canvas(height=526, width=800)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
card = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), tags="title")
card_word = canvas.create_text(400, 263, text='word', font=("Ariel", 60, "italic"), tags="prom")
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


right_button = Button(image=right_img, highlightthickness=0, command=save_progres)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=pick_random)

right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

pick_random()


window.mainloop()
