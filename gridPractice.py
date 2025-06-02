from tkinter import *
import random as r

def random():
    d1.set(r.randint(1,6))
    d2.set(r.randint(1,6))
    label_d1.config(text=d1.get())
    label_d2.config(text=d2.get())
    rollcount.set(rollcount.get()+1)
    label_rollcountvalue.config(text=rollcount.get())
    if d1.get()==6 and d2.get()==6:
        label_d1.config(bg='green')
        label_d2.config(bg='green')
    else:
        label_d1.config(bg='red')
        label_d2.config(bg='red')


root=Tk()
root.title('Dice Roll')
root.columnconfigure([0,1], minsize='150')
root.resizable(0,0)

PADDING=10
d1 = IntVar()
d1.set(0)
d2 = IntVar()
d2.set(0)
rollcount = IntVar()
rollcount.set(0)

button_quit = Button(root, text='Quit', command=root.destroy)
button_quit.grid(row=0,column=0, sticky='we', padx=PADDING, pady=PADDING)

button_random = Button(root, text='Random', command=random)
button_random.grid(row=0,column=1, sticky='we', padx=PADDING, pady=PADDING)

label_d1 = Label(root, background='red', text=0)
label_d1.grid(row=1,column=0,sticky='we', padx=PADDING, pady=1)

label_d2 = Label(root, background='red', text=0)
label_d2.grid(row=1,column=1,sticky='we', padx=PADDING, pady=1)

label_rollcount = Label(root, text='roll count =')
label_rollcount.grid(row=2,column=0,sticky='we', padx=PADDING, pady=1)

label_rollcountvalue = Label(root, text=0)
label_rollcountvalue.grid(row=2,column=1,sticky='we', padx=PADDING, pady=1)

root.mainloop()