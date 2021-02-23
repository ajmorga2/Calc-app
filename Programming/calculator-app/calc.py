from tkinter import *

root = Tk()



e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def button_clear():
    e.delete(0, END)
    
def button_add():
    first_num = e.get()
    global f_num
    global math
   # global decimal
    math = 'add'
    e.delete(0,END)
    f_num = int(first_num)
def button_sub():
    first_num = e.get()
    global f_num
    global math 
    math = 'subtract'
    e.delete(0,END)
    f_num = int(first_num)
def button_multi():
    first_num = e.get()
    global f_num
    global math 
    math = 'multiply'
    e.delete(0,END)
    f_num = int(first_num)
def button_div():
    first_num = e.get()
    global f_num
    global math
    math = 'divide'
    e.delete(0,END)
    f_num = int(first_num)
def button_neg_pos():
    num = e.get()
    e.delete(0,END)
    e.insert(0,str(int(num) * -1))
def button_percent():
    first_num = e.get()
    e.delete(0,END)
    f_num = int(first_num)
    e.insert(0,str(f_num * .01))
def button_deci():
    num = e.get()
    global new_num
    global decimal 
    new_num = float(num)
    decimal = 'deci'
    e.delete(0,END)
    e.insert(0,str(new_num + '.' ))
             
def button_equal():
    second_num = e.get()
    e.delete(0,END)
    if math == 'add':
        e.insert(0,f_num + int(second_num))
    elif math == 'subtract':
        e.insert(0,f_num - int(second_num))
    elif math == 'multiply':
        e.insert(0,f_num * int(second_num))
    elif math == 'divide':
        e.insert(0,f_num / int(second_num))
    elif math == 'add' and deciaml == 'deci':
        e.insert(0,new_num + float(second_num))
    
# define button
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text='+', padx=39, pady=20, command=button_add)
button_equals = Button(root, text='=', padx=39, pady=20, command=button_equal)
button_clear = Button(root, text='C', padx=40, pady=20, command=button_clear)

button_neg_pos = Button(root, text='+/-', padx=39, pady=20, command=button_neg_pos)
button_percent = Button(root, text='%', padx=39, pady=20, command=button_percent)
button_deci = Button(root, text='.', padx=39, pady=20, command=button_deci)



button_multi = Button(root, text='x', padx=39, pady=20, command=button_multi)
button_div = Button(root, text='÷', padx=39, pady=20, command=button_div)
button_sub = Button(root, text='-', padx=39, pady=20, command=button_sub)





#put buttons on screen
button_1.grid(row=4,column=0,sticky=NSEW)
button_2.grid(row=4,column=1,sticky=NSEW)
button_3.grid(row=4,column=2,sticky=NSEW)

button_4.grid(row=3,column=0,sticky=NSEW)
button_5.grid(row=3,column=1,sticky=NSEW)
button_6.grid(row=3,column=2,sticky=NSEW)

button_7.grid(row=2,column=0,sticky=NSEW)
button_8.grid(row=2,column=1,sticky=NSEW)
button_9.grid(row=2,column=2,sticky=NSEW)

button_0.grid(row=5,column=0,columnspan=2,sticky=NSEW)

button_add.grid(row=4,column=3,sticky=NSEW)
button_equals.grid(row=5,column=3,sticky=NSEW)
button_clear.grid(row=1,column=0,sticky=NSEW)

button_multi.grid(row=2,column=3,sticky=NSEW)
button_div.grid(row=1,column=3,sticky=NSEW)
button_sub.grid(row=3,column=3,sticky=NSEW)

button_neg_pos.grid(row=1,column=1,sticky=NSEW)
button_percent.grid(row=1,column=2,sticky=NSEW)
button_deci.grid(row=5,column=2,sticky=NSEW)


#button_add.grid
#button_equals.grid
#button_clear.grid


root.mainloop()