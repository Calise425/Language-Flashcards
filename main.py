from tkinter import *
import pandas
from random import randint
BACKGROUND_COLOR = "#B1DDC6"
# change language here
LANGUAGE = "korean"

# ----------------------------- DATA READING AND ORGANIZING ----------------------------- #

# Change this to change the language
# TODO add a dropdown for language changes?
words = pandas.read_csv(f"data/{LANGUAGE.lower()}_words.csv")
to_learn = words.to_dict()


def generate_word():
    # Getting the len - 1 for randomly generating an index
    dict_len = len(to_learn[f"{LANGUAGE.title()}"]) - 1
    canvas.itemconfig(language_text, text=LANGUAGE.title())
    canvas.itemconfig(word_text, text=to_learn[LANGUAGE.title()][randint(0, dict_len)].title())

    # TODO add window timeout for 3s to flip. Also want to include a function to flip card on card click


# ------------------------------ CARD SHOWING AND FLIPPING ------------------------------ #

# -------------------------------------- UI SETUP --------------------------------------- #
window = Tk()
window.title("Language Flashcards")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

canvas = Canvas(width=810, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(410, 260, image=card_front)
language_text = canvas.create_text(410, 170, text="Language here", font=('Arial', 20, 'italic'))
word_text = canvas.create_text(410, 260, text="Word", font=('Arial', 48, 'bold'))

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, border=0, command=generate_word)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, border=0, command=generate_word)

# Grid Layout
canvas.grid(column=0, row=0, columnspan=2)
wrong_button.grid(column=0, row=1,)
right_button.grid(column=1, row=1)

generate_word()
window.mainloop()
