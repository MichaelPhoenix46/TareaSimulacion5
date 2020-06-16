import tkinter as tk
import random as rand
from tkinter import *


root = tk.Tk()
root.geometry("1080x800")

canvas = tk.Canvas(root, width=800, height=800, bg="blue")
canvas.grid(row=6, column=1)

salami = canvas.create_rectangle(450, 400, 400, 450, fill="red")
canvas.moveto(salami, 0, 400)
empaque = canvas.create_rectangle(450, 400, 400, 450, fill="grey")
canvas.moveto(empaque, 400, 0)


lis = ["S", "M", "L"]


empaquetam = canvas.create_text(500, 20, font=('sans serif',30), text=rand.choice(lis))

speed1 = 10
speed2 = 10
productoscompletos = 0
productodanado = 0
empadanado = 0


#entries de velocidad


entry1 = tk.Entry(root)
entry1.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

entry1.insert(tk.END, 10)
entry2.insert(tk.END, 10)


#---------------

labelvelsal = tk.Label(root, text="velocidad de salami")
labelvelsal.grid(row=0, column=0)

labelvelsal = tk.Label(root, text="velocidad de empaque")
labelvelsal.grid(row=0, column=1)

label1 = tk.Label(root, text="Productos dañados")
label1.grid(row=4, column=0)

label2 = tk.Label(root, text="Productos completos")
label2.grid(row=4, column=1)

label3 = tk.Label(root, text="empaques dañados")
label3.grid(row=4, column=2)

#entries de resultados
entryprod = tk.Entry(root)
entryprod.grid(row=5, column=0)

entrycompl = tk.Entry(root)
entrycompl.grid(row=5, column=1)

entrypaq = tk.Entry(root)
entrypaq.grid(row=5, column=2)
#------------------

def Speed():
    global speed1
    global speed2
    s1 = entry1.get()
    s2 = entry2.get()
    speed1 = s1
    speed2 = s2
    if speed1 == speed2:
        canvas.moveto(salami, 0, 400)
        canvas.moveto(empaque, 400, 0)



button = tk.Button(root, text="cambiar velocidad", command=Speed)
button.grid(row=2, column=1)


def Movement():
    global productoscompletos
    global empadanado
    global productodanado
    #print(canvas.coords(empaque))
    canvas.move(salami, speed1, 0)
    #canvas.move(empaque, 0, 10)
    canvas.after(50, Movement2)
    if speed1 != speed2 and canvas.find_overlapping(*canvas.coords(empaque)) == canvas.find_overlapping(*canvas.coords(salami)):
        canvas.moveto(salami, 0, 400)
        canvas.moveto(empaque, 400, 0)
        canvas.itemconfig(empaquetam, text=rand.choice(lis))
        productodanado += 1
        empadanado += 1
        entrypaq.delete(0, END)
        entrypaq.insert(0, empadanado)
        entryprod.delete(0, END)
        entryprod.insert(0, productodanado)
        print("productos dañados", productodanado)
    if canvas.find_overlapping(*canvas.coords(empaque)) == canvas.find_overlapping(*canvas.coords(salami)) and canvas.itemcget(empaquetam, "text") == "L":
    #if canvas.coords(empaque) == canvas.coords(salami):
        canvas.moveto(salami, 0, 400)
        canvas.moveto(empaque, 400, 0)
        canvas.itemconfig(empaquetam, text=rand.choice(lis))
        productoscompletos += 1
        entrycompl.delete(0, END)
        entrycompl.insert(0, productoscompletos)
        print("productos completos", productoscompletos)
    elif canvas.find_overlapping(*canvas.coords(empaque)) == canvas.find_overlapping(*canvas.coords(salami)):
        canvas.moveto(salami, 0, 400)
        canvas.moveto(empaque, 400, 0)
        canvas.itemconfig(empaquetam, text=rand.choice(lis))
        empadanado += 1
        entrypaq.delete(0, END)
        entrypaq.insert(0, empadanado)
        print("empaque dañado", empadanado)
    if canvas.coords(salami)[0] > 750: #and canvas.coords(empaque)[1] > 750:
        canvas.moveto(salami, 0, 400)
        #canvas.moveto(empaque, 400, 0)


def Movement2():
    global count
    global empadanado
    canvas.move(empaque, 0, speed2)
    canvas.after(50, Movement)
    #if canvas.find_overlapping(*canvas.coords(empaque)) == canvas.find_overlapping(*canvas.coords(salami)):
     #   count += 1
      #  print(count)
    if canvas.coords(empaque)[1] > 750:
        canvas.moveto(empaque, 400, 0)
        canvas.itemconfig(empaquetam, text=rand.choice(lis))
        empadanado += 1
        entrypaq.delete(0, END)
        entrypaq.insert(0, empadanado)


Movement()
Movement2()

# this creates the loop that makes the window stay 'active'
root.mainloop()
