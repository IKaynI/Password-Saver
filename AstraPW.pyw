from tkinter import *
from random import *
import string
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from unittest import result
import os.path
import crypt
# --------------------------------------------------------------------------------------Fonctions ------------------------------------------------
def btn_clicked():
    pass
def taken():
    from crypt import cryptage
    freez_pass = password.get()
    website1 = website.get()
    if freez_pass and website1 != "":
        categorie = open("Mi_As/categorie.txt", "a")
        categorie.write(website1)
        categorie.write("\n")
        categorie.close()
        freez = open("Mi_As/freez.txt", "a")
        freez2 = cryptage(freez_pass)
        freez.write((freez2))
        freez.write("\n")
        freez.close()
        cat_recup()

def generer():
        entry2.delete(0, END)
        lenght = 14
        max_lenght = 15
        special_char = '&#%$'
        all_chars = string.ascii_letters + special_char + string.digits
        for x in range(randint(lenght, max_lenght)):
            password = "".join(choice(all_chars) for x in range(randint(lenght, max_lenght)))
        entry2.insert("end",password)
def cat_recup():
    if os.path.exists("Mi_As/categorie.txt") == True:
        with open('Mi_As/categorie.txt') as f:
            contents = f.read()
        if contents != "":
            entry0.delete("1.0", "end")
            count = 0
            file1 = open('Mi_As/categorie.txt', 'r')
            Lines = file1.readlines()
            for line in Lines:
                count += 1
                result = line.strip()
                entry0.insert("end",result + "\n")
def find_wp():
    from crypt import uncrypt
    website1 = website.get()
    verif = ""
    count = 0
    file1 = open('Mi_As/categorie.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        count += 1
        if line == website1 + "\n":
            verif = line
            break
    if verif == website1 + "\n":
        file2 = open('Mi_As/freez.txt')
        N_Lines = file2.readlines()
        count2 = 0
        for N_line in N_Lines:
            count2 = count2 + 1
            if count2 == count:
                entry2.delete(0, END)
                entry2.insert("end",uncrypt(N_line))
                break
# --------------------------------------------------------------------------------------Windows settings ------------------------------------------------

window = Tk()
window.geometry("859x591")
window.configure(bg = "#ffffff")
window.title("Password Saver by Astra")
window.iconbitmap('Verif_As/cyber.ico')
website = tk.StringVar()
password = tk.StringVar()
window_width = 859
window_height = 591
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# --------------------------------------------------------------------------------------Windows settings ------------------------------------------------
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 591,
    width = 859,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Pw_As/background.png")
background = canvas.create_image(
    429.5, 293.0,
    image=background_img)

entry0_img = PhotoImage(file = f"Pw_As/img_textBox0.png")
entry0_bg = canvas.create_image(
    700.0, 340.0,
    image = entry0_img)

entry0 = Text(
    width=30,
    height=12,
    bd = 0,
    bg = "#2D3032",
    highlightthickness = 0,
    fg="White",
    font= ("Helvetica", 15))

entry0.place(
    x = 644.0, y = 147,
    width = 112.0,
    height = 384)

entry1_img = PhotoImage(file = f"Pw_As/img_textBox1.png")
entry1_bg = canvas.create_image(
    139.5, 249.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#4a4f52",
    highlightthickness = 0,
    fg="White",
    font= ("Helvetica", 15),
    textvariable=website)

entry1.place(
    x = 65.0, y = 233,
    width = 149.0,
    height = 30)

entry2_img = PhotoImage(file = f"Pw_As/img_textBox2.png")
entry2_bg = canvas.create_image(
    409.5, 249.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#4a4f52",
    highlightthickness = 0,
    fg="White",
    font= ("Helvetica", 15),
    textvariable=password)

entry2.place(
    x = 304.0, y = 233,
    width = 211.0,
    height = 30)

img0 = PhotoImage(file = f"Pw_As/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = taken,
    relief = "flat")

b0.place(
    x = 53, y = 328,
    width = 172,
    height = 48)

img1 = PhotoImage(file = f"Pw_As/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = find_wp,
    relief = "flat")

b1.place(
    x = 53, y = 449,
    width = 172,
    height = 47)

img2 = PhotoImage(file = f"Pw_As/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = generer,
    relief = "flat")

b2.place(
    x = 339, y = 329,
    width = 171,
    height = 47)

window.resizable(False, False)
cat_recup()
window.mainloop()
