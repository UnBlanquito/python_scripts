from tkinter import *
from tkinter import ttk, messagebox
import googletrans  # pip install googletrans==4.0.0-rc1
from googletrans import Translator


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.config(text=c)
    label2.config(text=c1)
    root.after(1000, label_change)


def translate_now():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text

    text2.delete(1.0, END)
    text2.insert(END, trans_text)


root = Tk()
root.title("Google Translator 2.0")
root.geometry("920x400")
root.resizable(False, False)
root.config(background="white")

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

# first comboBox

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 12", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(
    root,
    text="English",
    font="segoe 30",
    bg="white",
    width=14,
    bd=2,
    relief=GROOVE,
)
label1.place(x=20, y=50)

# first comboBox

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 12", state="r")
combo2.place(x=610, y=20)
combo2.set("Select language")

label2 = Label(
    root,
    text="Spanish",
    font="segoe 30",
    bg="white",
    width=14,
    bd=2,
    relief=GROOVE,
)
label2.place(x=530, y=50)

# first frame
f = Frame(root, bg="white", bd=5)
f.place(x=10, y=118, width=400, height=210)

text1 = Text(f, font="Roboto 14", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=390, height=200)

Scrollbar1 = Scrollbar(f)
Scrollbar1.pack(side="right", fill="y")

Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)

# second frame

f1 = Frame(root, bg="white", bd=5)
f1.place(x=500, y=118, width=400, height=210)

text2 = Text(f1, font="Roboto 14", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=390, height=200)

Scrollbar2 = Scrollbar(f1)
Scrollbar2.pack(side="right", fill="y")

Scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=Scrollbar2.set)

# translate button

translate = Button(
    root,
    text="Translate",
    font=("Roboto", 15),
    activebackground="white",
    cursor="hand2",
    bd=1,
    width=8,
    height=1,
    bg="black",
    fg="white",
    command=translate_now,
)
translate.place(x=375, y=350)


# init

label_change()

root.mainloop()
