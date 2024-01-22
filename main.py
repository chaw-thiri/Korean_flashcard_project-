import random
from tkinter import *
import pandas as pd

# ----------------------------------------- Constants ----------------------------------------#
FONTNAME = "Ariel"
GREEN = "#B1DDC6"
timer = None
currentCard = {}
wordsToLearn = {}
# ---------------------------------------- READING DATABASE ---------------------------------#
try:
    df = pd.read_csv("data/new_word.csv")
except FileNotFoundError:
    orginalData = pd.read_csv("data/korean_vocab_1000.csv")
    wordsToLearn = orginalData.to_dict(orient="records")
else:
    wordsToLearn = df.to_dict(orient="records")
print(wordsToLearn)


# ---------------------------------------- WHEN EITHER OF THE BUTTON ARE CLICKED -----------#
def click():
    global timer
    global currentCard
    currentCard = random.choice(wordsToLearn)
    canvas.itemconfig(bgImg, image=flashcardFrontImg)
    canvas.itemconfig(cardTitle, text="Korean")
    canvas.itemconfig(cardWord, text=currentCard['Korean'])
    timer = window.after(3000, showAnswer)


# ---------------------------------- REMOVE THE CORRECT ANSWER FROM THE STUDY LIST __________#
def checked():
    wordsToLearn.remove(currentCard)
    print(len(wordsToLearn))
    data = pd.DataFrame(wordsToLearn )
    data.to_csv("data/new_word.csv",index=False)
    click()


# ---------------------------------- SHOW THE ANSWER __________________________________________#
def showAnswer():
    flashcardBackImg = PhotoImage("images/card_back.png")
    canvas.itemconfig(bgImg, image=flashcardBackImg)
    canvas.itemconfig(cardTitle, text="English")
    canvas.itemconfig(cardWord, text=currentCard['English'])


# -----------------------------------------UI setup-------------------------------------------#
window = Tk()
window.title("Learn 📗")
window.config(padx=50, pady=50, bg=GREEN)

# add flashcard img
canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
flashcardFrontImg = PhotoImage(file="images/card_front.png")
bgImg = canvas.create_image(400, 263, image=flashcardFrontImg)

# add words on the flash card
cardTitle = canvas.create_text(400, 158, text="Title", font=(FONTNAME, 40, "italic"))
cardWord = canvas.create_text(400, 263, text="Word", font=(FONTNAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# add right and wrong buttons
rightImg = PhotoImage(file="images/right.png")
wrongImg = PhotoImage(file="images/wrong.png")
rightButton = Button(image=rightImg, background=GREEN, highlightthickness=0, command=checked)
rightButton.grid(row=1, column=1)
wrongButton = Button(image=wrongImg, background=GREEN, highlightthickness=0, command=click)
wrongButton.grid(row=1, column=0)

click()
window.mainloop()
