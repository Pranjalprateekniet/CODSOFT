from tkinter import *
from PIL import Image,ImageTk
import random

root=Tk()
root.title("Rock Paper Scissor")
root.configure(background="#9b59b6")

# Load images
rock_image=ImageTk.PhotoImage(Image.open("rock_circle.png"))
paper_image=ImageTk.PhotoImage(Image.open("paper_circle.png"))
scissor_image=ImageTk.PhotoImage(Image.open("scissor_circle.png"))
rock_com=ImageTk.PhotoImage(Image.open("rock_cir.png"))
paper_com=ImageTk.PhotoImage(Image.open("papers_cir.png"))
scissor_com=ImageTk.PhotoImage(Image.open("scissor_cir.png"))

user_label=Label(root,image=scissor_image,bg="#9b59b6")
com_label=Label(root,image=scissor_com,bg="#9b59b6")
com_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
player_score=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computer_score=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

#button
rock=Button(root,width=20,height=2,text="Rock",bg="#FF3E4D",fg="white",command=lambda:update_choice("rock"))
paper=Button(root,width=20,height=2,text="Paper",bg="#7C7B1F",fg="white",command=lambda:update_choice("paper"))
scissor=Button(root,width=20,height=2,text="Scissor",bg="#1E0C4B",fg="white",command=lambda:update_choice("scissor"))
rock.grid(row=2,column=1)
paper.grid(row=2,column=2)
scissor.grid(row=2,column=3)

#indicator
user_indicator=Label(root,text="User",font=100,bg="#9b59b6",fg="white")
computer_indicator=Label(root,text="Computer",font=100,bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
computer_indicator.grid(row=0,column=1)

#message
msg=Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)

#update choices
choices=["rock","paper","scissor"]
def update_choice(x):
#this one is for computer choice
    com_choice=choices[random.randint(0,2)]
    if com_choice=="rock":
        com_label.configure(image=rock_com)
    elif com_choice=="paper":
        com_label.configure(image=paper_com)
    else:
        com_label.configure(image=scissor_com)
#for user choice
    if x=="rock":
        user_label.configure(image=rock_image)
    elif x=="paper":
        user_label.configure(image=paper_image)
    else:
        user_label.configure(image=scissor_image)
    check_win(x,com_choice)

#update messages
def update_message(x,col):
    msg['bg']=col
    msg['fg']="white"
    msg['font']=100
    msg['text']=x
#update scores
def update_userscore(x):
    score=int(player_score['text'])
    score+=1
    player_score['text']=str(score)
def update_computerscore(x):
    score=int(computer_score['text'])
    score+=1
    computer_score['text']=str(score)
#check winner
def check_win(player,computer):
    if player==computer:
        update_message("It's a Tie!","black")
    elif player=="rock":
        if computer=="scissor":
            update_message("You Win!","lightgreen")
            update_userscore(1)
        else:
            update_message("You Lose!","red")
            update_computerscore(1)
    elif player=="paper":
        if computer=="rock":
            update_message("You Win!","lightgreen")
            update_userscore(1)
        else:
            update_message("You Lose!","red")
            update_computerscore(1)
    elif player=="scissor":
        if computer=="paper":
            update_message("You Win!","lightgreen")
            update_userscore(1)
        else:
            update_message("You Lose!","red")
            update_computerscore(1)
    else:
        pass     

root.mainloop()