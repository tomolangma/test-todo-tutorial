import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("家庭用財産")

def test():
    x = ent.get()
    lbl["text"] = x
    pass


btn = tk.Button(root, text = "決定", command = test)
btn.place(x = 10,y = 10)
ent = tk.Entry(root, width = 10)
ent.place(x = 10, y = 50)
lbl = tk.Label(root, text = "0")
lbl.place(x = 10, y = 90)

root.mainloop()