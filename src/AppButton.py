import tkinter as tk
class AppButton(tk.Button):
    def __init__(self, master, text, command):
        super().__init__(
            master,
            text=text,
            command=command,
            width=24,
            bg="#2878c8",
            fg="white",
            activebackground="#1d5e9d",
            activeforeground="white",
            font=("Arial", 10),
            cursor="hand2",
        )
