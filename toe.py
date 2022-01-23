from importlib.machinery import WindowsRegistryFinder
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')

# X starts
clicked = True # boolean for X or O turn
count = 0 # to track the number of moves

# disable all the buttons
def disable_all_buttons():
    but1.config(state=DISABLED)
    but2.config(state=DISABLED)
    but3.config(state=DISABLED)
    but4.config(state=DISABLED)
    but5.config(state=DISABLED)
    but6.config(state=DISABLED)
    but7.config(state=DISABLED)
    but8.config(state=DISABLED)
    but9.config(state=DISABLED)

# check if someone won

def checkwin():
    global winner 
    winner = False

    if but1["text"]==but2["text"] and but2["text"]==but3["text"] and but1["text"]!=" ":
        but1.config(bg="green")
        but2.config(bg="green")
        but3.config(bg="green")
        winner = True
        winnersign = but1["text"]
    elif but4["text"]==but5["text"] and but5["text"]==but6["text"] and but4["text"]!=" ":
        but4.config(bg="green")
        but5.config(bg="green")
        but6.config(bg="green")
        winner = True
        winnersign = but4["text"]
    elif but7["text"]==but8["text"] and but8["text"]==but9["text"] and but7["text"]!=" ":
        but7.config(bg="green")
        but8.config(bg="green")
        but9.config(bg="green")
        winner = True
        winnersign = but7["text"]
    elif but1["text"]==but4["text"] and but4["text"]==but7["text"] and but1["text"]!=" ":
        but1.config(bg="green")
        but4.config(bg="green")
        but7.config(bg="green")
        winner = True
        winnersign = but1["text"]
    elif but2["text"]==but5["text"] and but5["text"]==but8["text"] and but2["text"]!=" ":
        but2.config(bg="green")
        but5.config(bg="green")
        but8.config(bg="green")
        winner = True
        winnersign = but2["text"]
    elif but3["text"]==but6["text"] and but6["text"]==but9["text"] and but3["text"]!=" ":
        but3.config(bg="green")
        but6.config(bg="green")
        but9.config(bg="green")
        winner = True
        winnersign = but3["text"]
    elif but1["text"]==but5["text"] and but5["text"]==but9["text"] and but1["text"]!=" ":
        but1.config(bg="green")
        but5.config(bg="green")
        but9.config(bg="green")
        winner = True
        winnersign = but1["text"]
    elif but3["text"]==but5["text"] and but5["text"]==but7["text"] and but3["text"]!=" ":
        but3.config(bg="green")
        but5.config(bg="green")
        but7.config(bg="green")
        winner = True
        winnersign = but3["text"]
    
    if winner == True:
        messagebox.showinfo("Tic Tac Toe", winnersign + " WINS!\nCongratulations")
        disable_all_buttons()
    elif count == 9: # check if tie
        messagebox.showinfo("Tic Tac Toe", "It's a TIE!\nNo one wins")
        disable_all_buttons()

# button click function
def but_click(b):
    global clicked, count
    
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1 
        checkwin()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkwin()
    else:
        messagebox.showerror("Tic Tac Toe", "Box already selected!\nPick another box")
# reset function to start over
def reset():
    global but1, but2, but3, but4, but5, but6, but7, but8, but9
    global clicked, count
    clicked = True
    count = 0
    # game buttons
    but1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: but_click(but1))
    but2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: but_click(but2))
    but3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: but_click(but3))

    but4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: but_click(but4))
    but5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: but_click(but5))
    but6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: but_click(but6))

    but7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: but_click(but7))
    but8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: but_click(but8))
    but9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: but_click(but9))

    # button grid 
    but1.grid(row=0, column=0)
    but2.grid(row=0, column=1)
    but3.grid(row=0, column=2)

    but4.grid(row=1, column=0)
    but5.grid(row=1, column=1)
    but6.grid(row=1, column=2)

    but7.grid(row=2, column=0)
    but8.grid(row=2, column=1)
    but9.grid(row=2, column=2)

# create menu to reset table after winning
my_menu = Menu(root)
root.config(menu=my_menu)

# create options
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)
reset()

root.mainloop()