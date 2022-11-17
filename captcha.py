import random # This random helps to give a random Module to the Captcha
from tkinter import *
import tkinter.messagebox # This import helps to give a Message box Module to the captcha

# Giving Text to the Captcha
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
root = Tk()

# Giving Title to the System
root.title("Captcha Application")
root.geometry("250x250")

# Stating that Captcha is StringVar
captcha = StringVar()

# Stating that user_input is StringVar
user_input = StringVar()

# This Function Generate the words to the Captcha
def set_captcha():
    s = random.choices(text)
    s += random.choices(text)
    s += random.choices(text)
    s += random.choices(text)
    s += random.choices(text)
    s += random.choices(text)
    captcha.set("".join(s))

# This Function Checks the Captcha and user_input are equal are not..
def check():
    ## If it is Equal
    if captcha.get() == user_input.get():
        tkinter.messagebox.showinfo("Sucess","Correct")
    ## If it is not Equal
    else:
        tkinter.messagebox.showerror("Error","Incorrect")
        set_captcha()

# This Widget Help to the set Things in Middle..
middleframe=Frame(root)
middleframe.pack(padx=10,pady=10)

# Giving Label to Captcha
Label(middleframe,textvariable = captcha, font = " Courier 30 overstrike bold",bg="yellow",relief=GROOVE).pack(pady=20)

# Giving entry to the user_input
Entry(middleframe,textvariable=user_input , font=" symbols 18").pack(padx=10)

# Giving button to the text Check
Button(middleframe,text ='Check',command=check, font=" Arial 13 bold").pack(pady=10)

set_captcha()
root.mainloop()