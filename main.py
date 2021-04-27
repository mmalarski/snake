from SnakeLogic import snakelogic
import tkinter as tk
import tkinter.font as font


def play_function(window_to_close):
    window_to_close.destroy()
    snakelogic()


def quit_function(window_to_close):
    window_to_close.destroy()


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

play_button = tk.Button(frame, command=lambda: play_function(window), font=font0, text="PLAY", width=6, height=1,
                        bg=buttoncolour, fg='lightblue')
play_button.pack(side=tk.TOP)

highscore_label = tk.Label(frame, font=font1, text="HIGHSCORE:", bg=background, fg='#1c632f')
highscore_label.pack(side=tk.TOP)

quit_button = tk.Button(frame, command=lambda: quit_function(window), font=font0, text="QUIT", width=6, height=1,
                        bg=buttoncolour, fg='lightblue')
quit_button.pack(side=tk.TOP)

window.mainloop()
