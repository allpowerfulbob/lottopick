# Copyright (c) Bob Sheets 2025 all rights reserved
# Powerball and Megamillions propety of their respective owners
# Import the tkinter module
import tkinter as tk
# Import the subprocess module
import subprocess as sp
# Import the tkterminal module
from tkterminal import Terminal
# Import the LottoPickMain module
import LottoPickMain

class LottoPick:
    def __init__(self, master):
        self.master = master
        self.master.title("Lotto Pick")

        def run_lotto_pick():
            sp.call(["python", "LottoPickMain.py"])

        def lotto_input():
            user_input = tk.entry.get()
            print(user_input)

        root = tk.Tk()
        root.title("Lotto Pick")
        root.geometry("400x400")
        root.configure(background="green")
        tk.Label(root, text ="Welcome to Lotto Pick!").pack()
        button = tk.Button(root, text="Generate Lotto Numbers", command=run_lotto_pick)
        button.pack()
        terminal = Terminal(root, width=80, height=20)
        terminal.pack()

        root.mainloop()