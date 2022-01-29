import tkinter as tk
from tkinter import messagebox
import pandas
import random

BG_COLOR = "#B1DDC6"
current_card = {}
csv_data = {}

try:
    csv_file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    csv_data = original_data.to_dict(orient="records")
else:
    csv_data = csv_file.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(csv_data)
    card.itemconfig(language, text="French", fill="black")
    card.itemconfig(card_word, text=current_card["French"], fill="black")
    card.itemconfig(card_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    card.itemconfig(card_img, image=card_back_img)
    card.itemconfig(language, text="English", fill="white")
    card.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    global current_card
    csv_data.remove(current_card)
    print(len(csv_data))
    data = pandas.DataFrame(csv_data)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


window = tk.Tk()
window.config(width=800, height=526, pady=50, padx=50, background=BG_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, flip_card)

ok_button_img = tk.PhotoImage(file="images/right.png")
ok_button = tk.Button(image=ok_button_img, highlightthickness=0, command=is_known)
ok_button.config(bg=BG_COLOR)
ok_button.grid(column=1, row=1)

wrong_button_img = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.config(bg=BG_COLOR)
wrong_button.grid(column=0, row=1)

card = tk.Canvas(width=800, height=500, highlightthickness=0)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_img = card.create_image(400, 250, image=card_front_img)
card.config(bg=BG_COLOR)
language = card.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
card_word = card.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

next_card()

window.mainloop()
