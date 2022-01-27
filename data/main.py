import tkinter as tk
from tkinter import messagebox
import pandas
import random


window = tk.Tk()
window.config(width=800, height=526, pady=50, padx=50)
window.title("Flashy")

ok_button_img = tk.PhotoImage(file="../images/right.png")
ok_button = tk.Button(image=ok_button_img, highlightthickness=0)
ok_button.grid(column=1, row=1)

wrong_button_img = tk.PhotoImage(file="../images/wrong.png")
wrong_button = tk.Button(image=wrong_button_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

card = tk.Canvas(width=800, height=500, highlightthickness=0)
card_img = tk.PhotoImage(file="../images/card_front.png")
card.create_image(400, 250, image=card_img)
card.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
card.create_text(400, 263, text="some word", fill="black", font=("Arial", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

# card_img = tk.PhotoImage(file="../images/card_back.png")
# card.create_text(400, 150, text="English", fill="black", font=("Arial", 40, "italic"))
# card.create_text(400, 263, text="some word", fill="black", font=("Arial", 60, "bold"))

try:
    csv_file = pandas.read_csv("french_words.csv")
except FileNotFoundError:
    messagebox.showinfo(title="Oops", message="There is no words to play!")
else:
    csv_data = csv_file.to_dict()
    eng_words = csv_data["English"]
    fr_words = csv_data["French"]


def pick_word():
    word_no = random.randint(0, len(eng_words))
    fr_word = fr_words[word_no]
    eng_word = eng_words[word_no]
    return fr_word, eng_word




window.mainloop()
