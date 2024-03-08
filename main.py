from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"


df = pandas.read_csv("data/french_words.csv")
french_dic = df.to_dict(orient="records")

def pick_random():
    random_word = random.choice(french_dic)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=random_word["French"])


def timer():
    txt = canvas.itemcget(card_word, "text")
    answer = ""
    for x in french_dic:
        if x['French'] == txt:
            answer = x['English']
    canvas.itemconfig(card, image=back_img)
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=answer)
    window.after(3000, timer)


def next_card():
    canvas.itemconfig(card, image=front_img)
    canvas.itemconfig(card_title, fill="black")
    canvas.itemconfig(card_word, fill="black")


def combine():
    pick_random()
    next_card()


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

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


right_button = Button(image=right_img, highlightthickness=0, command=combine)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=combine)

right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

pick_random()
window.after(3000, timer)

window.mainloop()
