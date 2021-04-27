import tkinter as tk
from tkinter import font
from SnakeLogic import snakelogic
import pygame, sys

background = '#3ec965'
buttoncolour = '#278b42'


def reopen_first_window(window_to_close):
    window_to_close.destroy()
    pygame.quit()
    first_window()


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

    retry_button = tk.Button(frame, font=font0, command=lambda: play_function(window), text="RETRY", width=6, height=1,
                             bg=buttoncolour, fg='lightblue')
    retry_button.grid(row=2, column=1)
    menu_button = tk.Button(frame, font=font0, command=lambda: reopen_first_window(window), text="MENU", width=6, height=1,
                            bg=buttoncolour, fg='lightblue')
    menu_button.grid(row=4, column=1)
    quit_button = tk.Button(frame, font=font0, command=lambda: quit_function(window), text="QUIT", width=6, height=1,
                            bg=buttoncolour, fg='lightblue')
    quit_button.grid(row=6, column=1)
    # label = tk.Label(frame)
    # label.grid(row=7, column=1)
    frame.grid_rowconfigure(1, minsize=5)
    frame.grid_rowconfigure(3, minsize=5)
    frame.grid_rowconfigure(5, minsize=5)
    frame.grid_rowconfigure(7, minsize=5)
    window.mainloop()


def play_function(window_to_close):
    window_to_close.destroy()
    pygame.quit()
    snakelogic()


def quit_function(window_to_close):
    window_to_close.destroy()
    sys.exit()


def first_window():
    background = '#3ec965'
    buttoncolour = '#278b42'

    window = tk.Tk()
    window.geometry("400x300")
    window.config(bg=background)
    window.title("Snake Game")

    frame = tk.Frame(window)
    frame.config(bg=background)
    frame.pack()
    frame.place(in_=window, anchor='c', relx=.5, rely=.5)

    font0 = font.Font(size=30, family='Roboto')
    font1 = font.Font(size=20, weight='bold', family='Roboto')

    play_button = tk.Button(frame, command=lambda: play_function(window), font=font0, text="PLAY", width=6,
                            height=1,
                            bg=buttoncolour, fg='lightblue')
    play_button.pack(side=tk.TOP)

    highscore_label = tk.Label(frame, font=font1, text="HIGHSCORE:", bg=background, fg='#1c632f')
    highscore_label.pack(side=tk.TOP)

    quit_button = tk.Button(frame, command=lambda: quit_function(window), font=font0, text="QUIT", width=6,
                            height=1,
                            bg=buttoncolour, fg='lightblue')
    quit_button.pack(side=tk.TOP)

    window.mainloop()

