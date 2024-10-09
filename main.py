import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}





def next_card():
    global current_card,after_flip
    window.after_cancel(after_flip)
    current_card = random.choice(to_learn)
    canvas.itemconfig(my_image, image=card_front)
    canvas.itemconfig(my_title, text = "French", fill = "black")
    canvas.itemconfig(my_text, text=current_card['French'], fill = "black")
    after_flip = window.after(3000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(my_image, image = card_back)
    canvas.itemconfig(my_title, text="English", fill="white")
    canvas.itemconfig(my_text, text=current_card['English'], fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()

after_flip = window.after(3000, flip_card)



window.title("Capstone")
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file = "images/card_back.png")
my_image = canvas.create_image(400, 263, image = card_front)
my_title = canvas.create_text(380, 150, text="Title", font=("Arial", 35, "bold"))
my_text = canvas.create_text(380, 250, text="Text", font=("Arial", 25))
canvas.grid(column=0, row=0, columnspan=2)

wrong_btn_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image = wrong_btn_image,highlightthickness=0, command=flip_card)
wrong_btn.grid(column=0, row=2)

right_btn_image = PhotoImage(file="images/right.png")
right_btn = Button(image = right_btn_image,highlightthickness=0, command=is_known)
right_btn.grid(column=1, row=2)



next_card()
window.mainloop()











































