from tkinter import *
import pandas
import random

bc = "#B1DDC6"
card = {}
tl = {}
try:
    dt1 = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    # dt = pandas.read_csv("data/hindi_words.csv")
    dt3 = pandas.read_csv("data/french_words.csv")
    tl = dt3.to_dict(orient="records")
else:
    tl = dt1.to_dict(orient="records")


def nxt():
    global card, tmr
    wd.after_cancel(tmr)
    card = random.choice(tl)
    ca.itemconfig(ctit, text="French", fill="black")
    ca.itemconfig(cwrd, text=card["French"], fill="black")
    ca.itemconfig(cbg, image=fimg)
    tmr = wd.after(1000, func=flip)

def flip():
    ca.itemconfig(ctit, text="English", fill="white")
    ca.itemconfig(cwrd, text=card["English"], fill="white")
    ca.itemconfig(cbg, image=bimg)

def know():
    tl.remove(card)
    d2 = pandas.DataFrame(tl)
    d2.to_csv("data/to_learn.csv", index=False)
    nxt()

wd = Tk()
wd.title("Aravindvas's Flash Cards")
wd.config(padx=50, pady=50, bg=bc)

tmr = wd.after(1000, func=flip)

ca = Canvas(width=800, height=526)
fimg = PhotoImage(file="images/card_front.png")
bimg = PhotoImage(file="images/card_back.png")
cbg = ca.create_image(400, 263, image=fimg)
ctit = ca.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
cwrd = ca.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
ca.config(bg=bc, highlightthickness=0)

ca.grid(row=0, column=0, columnspan=2)

wimg = PhotoImage(file="images/wrong.png")
wng = Button(image=wimg, highlightthickness=0, command=nxt)
wng.grid(row=1, column=0)

rimg = PhotoImage(file="images/right.png")
rt = Button(image=rimg, highlightthickness=0, command=know)
rt.grid(row=1, column=1)

nxt()



wd.mainloop()
