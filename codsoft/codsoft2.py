tkinter as tk
import tkinter.messagebox
window = tk.Tk()
window.title('simple calculator')
frame = tk.Frame(master = window,bg = "white",padx=10)
frame.pack()
entry = tk.Entry(master = frame,borderwidth = 3,width = 30)
entry.grid(row = 0,column = 0,columnspan = 3,ipady = 2,pady = 2)
def click(digit):
   entry.insert(tk.END,digit)
def clear():
    entry.delete(0,tk.END)
def equal():
    try: 
      a = str(eval(entry.get()))
      entry.delete(0,tk.END)
      entry.insert(0,a)
    except:
      tkinter.messagebox.showinginfo("syntax error")
      
b1 = tk.Button(master = frame,text = '1',padx = 15,pady = 5,width = 3, command = lambda:click(1))
b1.grid(row = 1,column = 0,pady = 2)
b2 = tk.Button(master = frame,text = '2',padx = 15,pady = 5,width = 3, command = lambda:click(2))
b2.grid(row = 1,column = 1,pady = 2)
b3 = tk.Button(master = frame,text = '3',padx = 15,pady = 5,width = 3, command = lambda:click(3))
b3.grid(row = 1,column = 2,pady = 2)
b4 = tk.Button(master = frame,text = '4',padx = 15,pady = 5,width = 3, command = lambda:click(4))
b4.grid(row = 2,column = 0,pady = 2)
b5 = tk.Button(master = frame,text = '5',padx = 15,pady = 5,width = 3, command = lambda:click(5))
b5.grid(row = 2,column = 1,pady =2) 
b6 = tk.Button(master = frame,text = '6',padx = 15,pady = 5,width = 3, command = lambda:click(6))
b6.grid(row = 2,column = 2,pady = 2)
b7 = tk.Button(master = frame,text = '7',padx = 15,pady = 5,width = 3, command = lambda:click(7))
b7.grid(row = 3,column = 0,pady = 2)
b8 = tk.Button(master = frame,text = '8',padx = 15,pady = 5,width = 3, command = lambda:click(8))
b8.grid(row = 3,column = 1,pady = 2)
b9 = tk.Button(master = frame,text = '9',padx = 15,pady = 5,width = 3, command = lambda:click(9))
b9.grid(row = 3,column = 2,pady = 2)
b0 = tk.Button(master = frame,text = '0',padx = 15,pady = 5,width = 3, command = lambda:click(0))