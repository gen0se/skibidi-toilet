import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(bg='#12f41f', width=700, height=700)
canvas.create_polygon(40,110,160,110,190,180,10,180,)
canvas.pack()
win.mainloop()