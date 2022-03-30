#
#

from tkinter import*

root=Tk()
root.title("Gui Puthon")
root.geometry("600x400")

btn=Button(text="Hello",
           background="#555",
           foreground="#ccc",
           padx="20",
           pady="8",
           font="16"
           )

btn.pack()

root.mainloop()