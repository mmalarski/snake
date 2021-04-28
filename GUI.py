import os
import tkinter as tk
from tkinter import font
from SnakeLogic import snakelogic
import pygame
import sys

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


def read():
    try:
        file = open('score.txt', 'r')
        filesize = os.path.getsize("score.txt")
        if filesize == 0:
            return 0
        else:
            return int(file.read())
    except FileNotFoundError:
        print("Nie istnieje plik.")


def first_window():
    window = tk.Tk()
    window.geometry("400x300")
    window.config(bg=background)
    window.title("Snake Game")

    text = tk.StringVar()
    text.set(read())

    frame = tk.Frame(window)
    frame.config(bg=background)
    frame.pack()
    frame.place(in_=window, anchor='c', relx=.5, rely=.5)

    font0 = font.Font(size=30, family='Roboto')
    font1 = font.Font(size=20, weight='bold', family='Roboto')

    play_button = tk.Button(frame, command=lambda: play_function(window), font=font0, text="PLAY", width=6,
                            height=1,
                            bg=buttoncolour, fg='lightblue')
    play_button.grid(row= 1, column=1)

    highscore_label1 = tk.Label(frame, font=font1, text="HIGHSCORE: ", bg=background, fg='#1c632f')
    highscore_label1.grid(row= 2, column=1)

    highscore_label2 = tk.Label(frame, font=font1, textvariable=text, bg=background, fg='#1c632f')
    highscore_label2.grid(row=2, column=2)

    quit_button = tk.Button(frame, command=lambda: quit_function(window), font=font0, text="QUIT", width=6,
                            height=1,
                            bg=buttoncolour, fg='lightblue')
    quit_button.grid(row= 3, column=1)

    window.mainloop()
