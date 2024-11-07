from tkinter import *
# Directory setup
import os
directory = os.getcwd() + f'/password-mgr/'
print(directory)



# ------------UI SETUP---------------
window = Tk()
window.title("MyPass")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="password-mgr/logo.png")
canvas.create_image(100, 100, image=logo)


window.mainloop()
