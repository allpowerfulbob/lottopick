# Import the tkinter module
import tkinter as tk
# Import the subprocess module
import subprocess as sp
# Import the LottoPickMain module
import LottoPickMain

root = tk.Tk()
root.title("Lotto Pick")
root.geometry("400x400")
root.configure(background="green")
tk.Label(root, text ="Welcome to Lotto Pick!").pack()
entry = tk.Entry(LottoPickMain.choice)
button = tk.Button(root, text="Generate Lotto Numbers", command=LottoPickMain.main)

root.mainloop()