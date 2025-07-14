import customtkinter as ctk
from tkinter import END,messagebox

def clear():
    entryField.delete(0,END)
def click(number):
    entryField.insert(END,number)
def answer():
    expression=entryField.get()
    try:
        result=eval(expression)
        ans=(round(result,2))
        entryField.delete(0,END)
        entryField.insert(0,ans)
    except SyntaxError:
        messagebox.showerror("Error","Invalid expression")
    except ZeroDivisionError:
        messagebox.showerror("Error","A number cannot be divided by zero")

root=ctk.CTk()
root.title("Calculator")
root.geometry("300x320")
root.config(bg="black")

entryField=ctk.CTkEntry(root,font=("Arial",20,"bold"),text_color="white",bg_color="black",border_color="white",width=280,height=50)
entryField.grid(row=0,column=0,padx=10,pady=10,columnspan=4)

b7=ctk.CTkButton(root,text='7',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command=lambda: click('7'))
b7.grid(row=1,column=0,pady=10)
b8=ctk.CTkButton(root,text='8',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command=lambda: click('8'))
b8.grid(row=1,column=1)
b9=ctk.CTkButton(root,text='9',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command=lambda: click('9'))
b9.grid(row=1,column=2)
bplus=ctk.CTkButton(root,text='+',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3',command=lambda: click('+'))
bplus.grid(row=1,column=3)

b6=ctk.CTkButton(root,text='6',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command=lambda: click('6'))
b6.grid(row=2,column=0,pady=10)
b5=ctk.CTkButton(root,text='5',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command=lambda: click('5'))
b5.grid(row=2,column=1)
b4=ctk.CTkButton(root,text='4',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command=lambda: click('4'))
b4.grid(row=2,column=2,pady=10)
bminus=ctk.CTkButton(root,text='-',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3',command=lambda: click('-'))
bminus.grid(row=2,column=3)

b3=ctk.CTkButton(root,text='3',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command=lambda: click('3'))
b3.grid(row=3,column=0,pady=10)
b2=ctk.CTkButton(root,text='2',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command=lambda: click('2'))
b2.grid(row=3,column=1)
b1=ctk.CTkButton(root,text='1',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command=lambda: click('1'))
b1.grid(row=3,column=2)
bmult=ctk.CTkButton(root,text='x',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3',command=lambda: click('*'))
bmult.grid(row=3,column=3)
 
b0=ctk.CTkButton(root,text='0',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command=lambda: click('0'))
b0.grid(row=4,column=0,pady=10)
bdot=ctk.CTkButton(root,text='.',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command=lambda: click('.'))
bdot.grid(row=4,column=1)
bclear=ctk.CTkButton(root,text='C',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='red',hover_color='red4',command=clear)
bclear.grid(row=4,column=2)
bdiv=ctk.CTkButton(root,text='/',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3',command=lambda: click('/'))
bdiv.grid(row=4,column=3)

bequal=ctk.CTkButton(root,text='=',font=('arial',20,'bold'),width=280,bg_color='black',cursor='hand2',fg_color='green',hover_color='green4',command=answer)
bequal.grid(row=5,column=0,columnspan=4,pady=10)

def key_input(event):
    key = event.char
    if key in '0123456789.+-*/':
        click(key)
    elif event.keysym == 'Return':
        answer()
    elif event.keysym in ['BackSpace', 'Delete']:
        current = entryField.get()
        entryField.delete(0, END)
        entryField.insert(0, current[:-1])
    elif key.lower() == 'c':
        clear()

root.bind('<Key>', key_input)



root.mainloop()