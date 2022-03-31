#
#

from tkinter import*

clicks=0

def click_button():
    global clicks
    clicks=clicks+1
    btn.config(text="Clicks {}".format(clicks))

root=Tk()
root.title("Gui Puthon")
root.geometry("600x400")

btn=Button(text="Hello",
           background="#555",
           foreground="#ccc",
           padx="20",
           pady="8",
           font="16",
           command=click_button
           )

btn.pack()

root.mainloop()