import tkinter as tk
class AppLabel(tk.Label):
    def __init__(self, master, text):
        super().__init__(
            master,
            text=text,
            bg="#f0f0f0",
            fg="#222222",
            font=("Arial", 11),
            anchor="w",
        )
