from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

root = Tk()
root.title("Tic-Tac-Toe")
root.geometry("286x343+0+0")
root.resizable(False,False)

p1 = simpledialog.askstring("Tic-Tac-Toe","Whats's first player name?",parent=root)
p2 = simpledialog.askstring("Tic-Tac-Toe","Whats's second player name?",parent=root)

x = "O"

def clearbrd():
    btn1["text"] = "  "
    btn2["text"] = "  "
    btn3["text"] = "  "
    btn4["text"] = "  "
    btn5["text"] = "  "
    btn6["text"] = "  "
    btn7["text"] = "  "
    btn8["text"] = "  "
    btn9["text"] = "  "

def checkwin():
    if (btn1["text"] == btn2["text"] == btn3["text"] != "  " or
        btn4["text"] == btn5["text"] == btn6["text"] != "  " or
        btn7["text"] == btn8["text"] == btn9["text"] != "  " or
        btn1["text"] == btn4["text"] == btn7["text"] != "  " or
        btn2["text"] == btn5["text"] == btn8["text"] != "  " or
        btn3["text"] == btn6["text"] == btn9["text"] != "  " or
        btn1["text"] == btn5["text"] == btn9["text"] != "  " or
        btn3["text"] == btn5["text"] == btn7["text"] != "  "):
        if x == "X":
            messagebox.showinfo("Tic-Tac-Toe",p1+" won!")
        elif x == "O":
            messagebox.showinfo("Tic-Tac-Toe",p2+" won!")
        clearbrd()
    elif (btn1["text"] != "  " and btn2["text"] != "  " and btn3["text"] != "  " and
          btn4["text"] != "  " and btn5["text"] != "  " and btn6["text"] != "  " and
          btn7["text"] != "  " and btn8["text"] != "  " and btn9["text"] != "  "):
        messagebox.showinfo("Tic-Tac-Toe","That\'s a tie!")
        clearbrd()

def onclick(btn):
    global x
    if x == "X":
        x = "O"
    else:
        x = "X"
    if btn["text"] == "  ":
        btn["text"] = x
    checkwin()
    

btn1 = Button(root,font=("arial",20,"bold"),text="  ",bg="white",width=5,pady=30,command=lambda: onclick(btn1))
btn1.grid(row=0,column=0)
btn2 = Button(root,font=("arial",20,"bold"),text="  ",bg="white",width=5,pady=30,command=lambda: onclick(btn2))
btn2.grid(row=0,column=1)
btn3 = Button(root,font=("arial",20,"bold"),text="  ",bg="white",width=5,pady=30,command=lambda: onclick(btn3))
btn3.grid(row=0,column=2)

btn4 = Button(root,font=("arial",20,"bold"),text="  ",bg="white",width=5,pady=30,command=lambda: onclick(btn4))
btn4.grid(row=1,column=0)
btn5 = Button(root,font=("arial",20,"bold"),text="  ",bg="white",width=5,pady=30,command=lambda: onclick(btn5))
btn5.grid(row=1,column=1)
btn6 = Button(root,font=("arial",20,"bold"),text="  ",bg="white",width=5,pady=30,command=lambda: onclick(btn6))
btn6.grid(row=1,column=2)

btn7 = Button(root,font=("arial",20,"bold"),text="  ",bg="white",width=5,pady=30,command=lambda: onclick(btn7))
btn7.grid(row=2,column=0)
btn8 = Button(root,font=("arial",20,"bold"),text="  ",bg="white",width=5,pady=30,command=lambda: onclick(btn8))
btn8.grid(row=2,column=1)
btn9 = Button(root,font=("arial",20,"bold"),text="  ",bg="white",width=5,pady=30,command=lambda: onclick(btn9))
btn9.grid(row=2,column=2)

root.mainloop
