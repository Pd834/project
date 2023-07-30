import from tkinter  *
def add(entry:Entry,listbox:Listbox):
    new = entry.get()
    listbox.insert(END,new)
    
def delete(listbox:Listbox):
    listbox.delete(ACTIVE)

root = Tk()
root.title('TO-DO-LIST')
root.geometry('300x400')
root.resizable(0,0)
Label(root,text='TO-DO-LIST',bg="blue")
scrollbar=Listbox(root,bg='gold',height=14,width=25)from tkinter i
new_item=Entry(root,width=30)
add_btn=Button(root,text='add item',bg='blue',width=10,command=lambda:add(new_item_entry,tasks))
delete_btn=Button(root,text='delete item',bg='blue',width=10,command=lambda:delete(tasks)) 
root.mainloop                           
