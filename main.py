from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ----------------------------- DATA READING AND ORGANIZING ----------------------------- #

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
wrong_button = Button(image=wrong_img, highlightthickness=0, border=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, border=0)

# Grid Layout
canvas.grid(column=0, row=0, columnspan=2)
wrong_button.grid(column=0, row=1,)
right_button.grid(column=1, row=1)

window.mainloop()
