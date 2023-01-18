from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from turtle import color



root=Tk()
root.title("White Board | Developed by Sukalyan")
root.geometry("1050x570+130+50")
root.resizable(False,False)
root.config(background='black')

#Function defining
current_x=0
current_y=0
color="Black"
def show_color(new_color):
    global color
    color=new_color

def locate_xy(work):
    global current_y,current_x
    current_x=work.x
    current_y=work.y


def addLine(work):
    global current_y, current_x
    canvas.create_line(current_x,current_y,work.x,work.y,width=get_current_value(),fill=color)
    current_x=work.x
    current_y=work.y

def new_canvas():
    canvas.delete("all")
    color_palete()

#For loading the images
logo=PhotoImage(file="logo.png")
root.iconphoto(False,logo)

color_panel=PhotoImage(file="color section.png")
Label(root,image=color_panel,bg='#f2f3f5').place(x=10,y=20)

eraser=PhotoImage(file="eraser.png")
Button(root,image=eraser,bg='#f2f3f5',command=new_canvas).place(x=30,y=400)

#color palet
colors=Canvas(root,bg='#f2f3f5',height=300,width=37,border=10,bd=0)
colors.place(x=30,y=60)

#board
canvas=Canvas(root,bg='white',height=460,width=880,border=10,bd=25,relief=RIDGE,cursor='hand2')
canvas.place(x=100,y=35)
canvas.bind("<Button-1>",locate_xy)
canvas.bind("<B1-Motion>",addLine)

#Filling colors in the color pallet
def color_palete():
    id=colors.create_rectangle((10,10,30,30),fill="Black")
    colors.tag_bind(id,"<Button-1>",lambda x:show_color("Black"))

    id = colors.create_rectangle((10, 40, 30, 60), fill="red")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("red"))

    id = colors.create_rectangle((10, 70, 30, 90), fill="yellow")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("yellow"))

    id = colors.create_rectangle((10, 100, 30, 120), fill="blue")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("blue"))

    id = colors.create_rectangle((10, 130, 30, 150), fill="grey")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("grey"))

    id = colors.create_rectangle((10, 160, 30, 180), fill="white")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("white"))

    id = colors.create_rectangle((10, 190, 30, 210), fill="green")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("green"))

    id = colors.create_rectangle((10, 220, 30, 240), fill="orange")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("orange"))

    id = colors.create_rectangle((10, 250, 30, 270), fill="pink")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("pink"))

    id = colors.create_rectangle((10, 280, 30, 300), fill="purple")
    colors.tag_bind(id, "<Button-1>", lambda x: show_color("purple"))

color_palete()

def slider_change(event):
    value_lable.configure(text=get_current_value())

#Adding the slider
current_value=tk.DoubleVar()
slider=ttk.Scale(root,from_=0,to=100,orient=HORIZONTAL,command=slider_change,variable=current_value)
slider.place(x=0,y=520)

def get_current_value():
    return '{: .2f}'.format(current_value.get())


value_lable=ttk.Label(root,text=get_current_value())
value_lable.place(x=27,y=540)




root.mainloop()