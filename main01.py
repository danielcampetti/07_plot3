# Programa 1

v6

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Aplicativo Nieto Engenharia")
root.iconbitmap('.//img//logo.ico')
root.geometry("400x400")


button_quit = Button(root, text="Fechar Programa", command=root.quit)
button_quit.pack()

root.mainloop()
