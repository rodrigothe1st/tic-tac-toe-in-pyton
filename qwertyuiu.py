import tkinter as tk
from time import *
color = 1
clicked_boxes = set()
red = set()
blue = set()
plays = 0

def reset():
    global color, clicked_boxes, red, blue, plays
    color = 1
    clicked_boxes.clear()
    red.clear()
    blue.clear()
    plays = 0
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.configure(bg="gray")

def click(event):
    global color, plays
    if event.widget in clicked_boxes:
        return
    clicked_boxes.add(event.widget)
    color = (color + 1) % 2
    plays += 1
    event.widget.configure(bg="blue" if color == 0 else "red")
    if color == 0:
        blue.add(event.widget.pos)
    else:
        red.add(event.widget.pos)
    if (a0 in red and a1 in red and a2 in red) or (b0 in red and b1 in red and b2 in red) or (c0 in red and c1 in red and c2 in red) or (a0 in red and b0 in red and c0 in red) or (a1 in red and b1 in red and c1 in red) or (a2 in red and b2 in red and c2 in red) or (a0 in red and b1 in red and c2 in red) or (a2 in red and b1 in red and c0 in red):
        print("Red Wins!")
        for widget in root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg="red")
                
                

    elif (a0 in blue and a1 in blue and a2 in blue) or (b0 in blue and b1 in blue and b2 in blue) or (c0 in blue and c1 in blue and c2 in blue) or (a0 in blue and b0 in blue and c0 in blue) or (a1 in blue and b1 in blue and c1 in blue) or (a2 in blue and b2 in blue and c2 in blue) or (a0 in blue and b1 in blue and c2 in blue) or (a2 in blue and b1 in blue and c0 in blue):
        print("Blue Wins!")
        for widget in root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg="blue")
                
                
    elif plays == 9:
        print("It's a Draw!")
        
        reset()
root = tk.Tk()
# First row
a0 = tk.Label(root, width=6, height=2, background="gray")
a0.grid(padx=5, pady=5,row=0, column=0 )
a0.bind("<Button-1>", click)
a1 = tk.Label(root, width=6, height=2, background="gray")
a1.grid(padx=5, pady=5, row=0, column=1)
a1.bind("<Button-1>", click)
a2 = tk.Label(root, width=6, height=2, background="gray")
a2.grid(padx=5, pady=5, row=0, column=2)
a2.bind("<Button-1>", click)
# Second row
b0 = tk.Label(root, width=6, height=2, background="gray")
b0.grid(padx=5, pady=5, row=1, column=0)
b0.bind("<Button-1>", click)
b1 = tk.Label(root, width=6, height=2, background="gray")
b1.grid(padx=5, pady=5, row=1, column=1)
b1.bind("<Button-1>", click)
b2 = tk.Label(root, width=6, height=2, background="gray")
b2.grid(padx=5, pady=5, row=1, column=2)
b2.bind("<Button-1>", click)
# Third row
c0 = tk.Label(root, width=6, height=2, background="gray")
c0.grid(padx=5, pady=5, row=2, column=0)
c0.bind("<Button-1>", click)
c1 = tk.Label(root, width=6, height=2, background="gray")
c1.grid(padx=5, pady=5, row=2, column=1)
c1.bind("<Button-1>", click)
c2 = tk.Label(root, width=6, height=2, background="gray")
c2.grid(padx=5, pady=5, row=2, column=2)
c2.bind("<Button-1>", click)
#  
a0.pos = a0
a1.pos = a1
a2.pos = a2
b0.pos = b0
b1.pos = b1
b2.pos = b2
c0.pos = c0
c1.pos = c1
c2.pos = c2
#
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(padx=5, pady=5, row=3, column=1)
lbl=tk.Label(root)


root.mainloop()
