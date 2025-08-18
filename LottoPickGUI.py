# Copyright (c) Bob Sheets 2025 all rights reserved
# Powerball and Megamillions propety of their respective owners
# Import the tkinter module
import tkinter as tk
# Import tkterminal
from tkterminal import Terminal
# Import the subprocess module
import subprocess as sp
# Import the LottoPickMain module
import LottoPickMain

def run_lotto_pick():
    sp.call(["python", "LottoPickMain.py"])

root = tk.Tk()
root.title("Lotto Pick")
root.geometry("400x400")
root.configure(background="green")
tk.Label(root, text ="Welcome to Lotto Pick!").pack()
button = tk.Button(root, text="Generate Lotto Numbers", command=run_lotto_pick)
button.pack()
terminal = Terminal(root)
terminal.pack(expand=True, fill=tk.BOTH)

root.mainloop()