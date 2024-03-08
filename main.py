from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"
# change language here
LANGUAGE = "korean"
# TODO add a dropdown for language changes?
# TODO change the card flip functionality to trigger on card click, not after time

# ----------------------------- DATA READING AND ORGANIZING ----------------------------- #
try:
    with open(f"data/words_to_learn_{LANGUAGE}.csv", mode="r", encoding="utf-8") as file:
        data = pandas.read_csv(file, encoding="utf-8")
        to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv(f"data/{LANGUAGE.lower()}_words.csv", encoding="utf-8")
    to_learn = data.to_dict(orient="records")
finally:
    current_card = {}


def close():
    """Closes the application and saves the current 'to_learn' as a json file"""
    print("close triggered")
    to_learn_df = pandas.DataFrame(to_learn)
    to_learn_df.to_csv(f"data/words_to_learn_{LANGUAGE}.csv", index=False, encoding="utf-8")
    window.quit()


# ------------------------------ CARD SHOWING AND FLIPPING ------------------------------ #

def generate_word():
    """Chooses a random dictionary from the to_learn and changes the canvas text to display that word"""
    global current_card, flip_timer
    # this makes it so that if you flip to a new card it starts the timer again
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    word_to_translate = current_card[LANGUAGE.title()].title()
    canvas.itemconfig(canvas_card, image=card_front)
    canvas.itemconfig(language_text, text=LANGUAGE.title())
    canvas.itemconfig(word_text, text=word_to_translate)
    flip_timer = window.after(3000, flip_card, current_card)


def flip_card(card):
    """Shows the other side of the card with the english word"""
    word_eng = card["English"].title()
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=word_eng)
    canvas.itemconfig(canvas_card, image=card_back)


def checkmark():
    """run when the user knows the word and hits the checkmark, removing the word from to_learn"""
    global current_card
    to_learn.remove(current_card)
    generate_word()


# -------------------------------------- UI SETUP --------------------------------------- #
window = Tk()
window.title("Language Flashcards")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card, current_card)

canvas = Canvas(width=810, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_card = canvas.create_image(410, 260, image=card_front)
language_text = canvas.create_text(410, 170, text="Language here", font=('Arial', 20, 'italic'))
word_text = canvas.create_text(410, 260, text="Word", font=('Arial', 48, 'bold'))

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, border=0, command=generate_word)
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, border=0, command=checkmark)

# Grid Layout
canvas.grid(column=0, row=0, columnspan=2)
wrong_button.grid(column=0, row=1,)
right_button.grid(column=1, row=1)

window.protocol("WM_DELETE_WINDOW", close)

generate_word()
window.mainloop()
