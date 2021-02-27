import tkinter as tk
from tkinter import simpledialog
from tkinter.messagebox import showerror
class MyDialog(simpledialog.Dialog):
    def body(self, master):
        self.wm_geometry("350x150+820+800")
        tk.Label(master, text="Please Choose Defficulty Level:").grid(row=0)
        self.e1 = tk.Entry(master)
        tk.Label(master, text="1 For Beginner").grid(row=1)
        self.e1 = tk.Entry(master)
        tk.Label(master, text="2 For Intermediate").grid(row=2)
        self.e1 = tk.Entry(master)
        tk.Label(master, text="3 For Hard").grid(row=3)
        self.e1 = tk.Entry(master)
        self.e1.grid(row=4, column=0)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        self.result = first
        return self.result
   