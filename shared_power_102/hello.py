from tkinter import *
from PIL import ImageTk
# import PIL

root = Tk()
root.geometry('1000x1000')
image = ImageTk.PhotoImage()
print(image)
print(type(image))
label = Label(root, image=image)
label.place(x=0, y=0)
root.mainloop()