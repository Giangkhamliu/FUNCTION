from tkinter import *
gui=Tk()
gui.title("Grace Calculator")
e=Entry (gui,width=25,borderwidth=12,bg="light blue",fg="black")
e.grid(row=0,column=0,columnspan=4,padx=30,pady=25)
def button_click(number):
    new_num=e.get()
    e.delete(0,END)
    e.insert(0,str(new_num)+ str(number))
    num_1=e.get()
    global f_num
    global math
    f_num=int(num_1)
    math="addition" 
    math="multiplication" 
    math="division" 
    math="subtraction" 
def b_add():
    if math=="addition":
          e.insert(f_num+f_num2)
          e.delete(0,END)
def b_subtract():
    if math=="subtraction":
        e.insert(0,f_num-f_num2)
        e.delete(0,END)
def b_multiply():
    if math=="multiplication":
        e.insert(0,f_num*f_num2)
        e.delete(0,END)
def b_clear():
    e.delete(0,END)
def b_divide():
    if math=="division":
        e.insert(0,f_num/f_num2)
        e.delete(0,END)
def b_equal():
    num_2=e.get()
    global f_num2
    f_num2=int(num_2)
    e.delete(0,END)
    e.insert(0,f_num+f_num2)
b_1=Button(gui,text="1",bg="light green",fg="black",padx=25,pady=30,command=lambda:button_click(1))
b_1.grid(row=4,column=0)
b_2=Button(gui,text="2",bg="light green",fg="black",padx=25,pady=30,command=lambda:button_click(2))
b_2.grid(row=4,column=1)
b_3=Button(gui,text="3",bg="light green",fg="black",padx=25,pady=30,command=lambda:button_click(3))
b_3.grid(row=4,column=2)
b_4=Button(gui,text="4",bg="light pink",fg="black",padx=25,pady=30,command=lambda:button_click(4))
b_4.grid(row=3,column=0)
b_5=Button(gui,text="5",bg="light pink",fg="black",padx=25,pady=30,command=lambda:button_click(5))
b_5.grid(row=3,column=1)
b_6=Button(gui,text="6",bg="light pink",fg="black",padx=25,pady=30,command=lambda:button_click(6))
b_6.grid(row=3,column=2)
b_7=Button(gui,text="7",bg="white",fg="black",padx=25,pady=30,command=lambda:button_click(7))
b_7.grid(row=2,column=0)
b_8=Button(gui,text="8",bg="white",fg="black",padx=25,pady=30,command=lambda:button_click(8))
b_8.grid(row=2,column=1)
b_9=Button(gui,text="9",bg="white",fg="black",padx=25,pady=30,command=lambda:button_click(9))
b_9.grid(row=2,column=2)
b_0=Button(gui,text="0",bg="light green",fg="black",padx=25,pady=30,command=lambda:button_click(0))
b_0.grid(row=4,column=3)
b_clear=Button(gui,text="AC",bg="orange",fg="black",padx=20,pady=25,command=b_clear)
b_clear.grid(row=1,column=0)
b_equal=Button(gui,text="=",bg="orange",fg="black",padx=20,pady=25,command=b_equal)
b_equal.grid(row=1,column=3)
b_divide=Button(gui,text="%",bg="orange",fg="black",padx=20,pady=25,command=b_divide)
b_divide.grid(row=1,column=2)
b_multiply=Button(gui,text="x",bg="orange",fg="black",padx=20,pady=25,command=b_multiply)
b_multiply.grid(row=2, column=3)
b_subtract=Button(gui,text="-",bg="orange",fg="black",padx=20,pady=25,command=b_subtract)
b_subtract.grid(row=3,column=3)
b_add=Button(gui,text="+",bg="orange",fg="black",padx=20,pady=25,command=b_add)
b_add.grid(row=1,column=1)
gui.mainloop()

