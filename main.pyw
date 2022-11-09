from tkinter import *
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import os
import linecache
# ------------------------------------------------------------------------Fonction Login --------------------------------------------------------
def start_menu():
    print("Réussi")
# ------------------------------------------------------------------------Fonction Login --------------------------------------------------------
def btn_clicked():
    from crypt import uncrypt
    from crypt import cryptage
    User_info = open("Mi_As/user.txt", "a")
    User_info.close()
    User_name = username.get()
    User_pswd = password.get()
    with open('Mi_As/user.txt') as f:
        contents = f.read()
        line_us = linecache.getline('Mi_As/user.txt', 1)
        line_pw = linecache.getline('Mi_As/user.txt', 2)
        verif_user = line_us 
        verif_pswd = line_pw
    if contents != "":
        Un_User = uncrypt(verif_user)
        print(Un_User)
        Un_pswd = uncrypt(verif_pswd)
        if Un_User == User_name:
            if Un_pswd == User_pswd:
                window.destroy()
                os.system('python AstraPW.pyw')
    if contents == "":
        User_info = open("Mi_As/user.txt", "a")
        Crypt_User = cryptage(User_name)
        Crypt_pswd = cryptage(User_pswd)
        User_info.write(Crypt_User)
        User_info.write("\n")
        User_info.write(Crypt_pswd)
        messagebox.showinfo("Information", "The creation of your account has been a success ! Rerty the software.")
        window.destroy()
             
    if contents != "":
        if Un_pswd  != User_pswd:
            messagebox.showwarning("Error", "Password Incorrect")
#---------------------------------------------------------------WINDOW Settings-----------------------------------------------------
window = Tk()
window.title("Astra Verification")
window.geometry("701x409")
window.configure(bg = "#ffffff")
window_width = 701
window_height = 409
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.iconbitmap('Verif_As/cyber.ico')
# --
username = tk.StringVar()
password = tk.StringVar()
#---------------------------------------------------------------WINDOW Settings-----------------------------------------------------
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 409,
    width = 701,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"Verif_As/background.png")
background = canvas.create_image(
    351.0, 197.0,
    image=background_img)

img0 = PhotoImage(file = f"Verif_As/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 475, y = 345,
    width = 147,
    height = 33)

entry0_img = PhotoImage(file = f"Verif_As/img_textBox0.png")
entry0_bg = canvas.create_image(
    548.5, 304.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#515768",
    highlightthickness = 0,
    fg= "white",
    font= ("Helvetica", 14),
    show="*",
    textvariable=password)

entry0.place(
    x = 456.0, y = 289,
    width = 185.0,
    height = 28)

entry1_img = PhotoImage(file = f"Verif_As/img_textBox1.png")
entry1_bg = canvas.create_image(
    548.5, 209.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#515768",
    highlightthickness = 0,
    fg= "white",
    font= ("Helvetica", 14),
    textvariable=username,)

entry1.place(
    x = 456.0, y = 194,
    width = 185.0,
    height = 28)

window.resizable(False, False)
window.mainloop()
