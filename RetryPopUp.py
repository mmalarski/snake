import tkinter as tk
from tkinter import font

background = '#3ec965'
buttoncolour = '#278b42'


def retry():
    window = tk.Tk()
    window.geometry("400x300")
    window.config(bg=background)
    window.title("You lost")

    frame = tk.Frame(window)
    frame.config(bg=background)
    frame.pack()
    frame.place(in_=window, anchor='c', relx=.5, rely=.5)

    font0 = font.Font(size=30, family='Roboto')

    retry_button = tk.Button(frame, font=font0, text="RETRY", width=6, height=1,
                             bg=buttoncolour, fg='lightblue')
    retry_button.grid(row=2, column=1)
    menu_button = tk.Button(frame, font=font0, text="MENU", width=6, height=1,
                            bg=buttoncolour, fg='lightblue')
    menu_button.grid(row=4, column=1)
    quit_button = tk.Button(frame, font=font0, text="QUIT", width=6, height=1,
                            bg=buttoncolour, fg='lightblue')
    quit_button.grid(row=6, column=1)
    # label = tk.Label(frame)
    # label.grid(row=7, column=1)
    frame.grid_rowconfigure(1, minsize=5)
    frame.grid_rowconfigure(3, minsize=5)
    frame.grid_rowconfigure(5, minsize=5)
    frame.grid_rowconfigure(7, minsize=5)
    window.mainloop()
