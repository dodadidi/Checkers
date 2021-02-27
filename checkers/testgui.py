from tkinter import * #tkinter from simpledialog library is used to take from the human the difficulty level he wantsthe game to be.
import tkinter as tk
#from tkinter import messagebox


def main():
    opening_window = tk.Tk()
    
    opening_window.configure(width=700,height=100)
    opening_window.geometry("700x100")
    opening_window.withdraw()
    root = Tk()

    e = Entry(root,width=300, bg = "blue", fg = "red")
    e.pack()

    def myClick():
        myLbl  = Label(root, text = "i clicked...")
        myLbl.pack()

    myBtn = Button(root, text="Cancel", command=myClick)
    myBtn.pack()
    root.mainloop()