from SnakeLogic import snakelogic
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.config(bg='lightgreen')
window.title("Snake Game")

frame = tk.Frame(window)
frame.pack()

play_button = tk.Button(frame, text="PLAY", width=40, height=7, bg='green', fg='blue')
play_button.pack(side=tk.TOP)

highscore_label = tk.Label(frame, text="HIGHSCORE", bg='green', fg='blue')
highscore_label.pack(side=tk.TOP)

quit_button = tk.Button(frame, text="QUIT", width=40, height=7, bg='green', fg='blue')
quit_button.pack(side=tk.TOP)

window.mainloop()
