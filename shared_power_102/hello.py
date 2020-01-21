from tkinter.ttk import *
from tkinter import *

root = Tk()
tree = ttk.Treeview(root)
tree["columns"] = ("one", "two", "three")
tree.column("#0", width=270, minwidth=270, stretch=NO)
tree.column("one", width=150, minwidth=150, stretch=NO)
tree.column("two", width=400, minwidth=200)
tree.column("#0", width=400, minwidth=50, stretch=NO)
# tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
root.mainloop()