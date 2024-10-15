from tkinter import *

def buttons(num):
    global equation_text
    
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equalsto():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text = ""

    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

root = Tk()
root.title("Calculator Program")
root.geometry("500x500")

equation_label = StringVar()
equation_text = ""

label = Label(root, textvariable= equation_label, font= ('consolas', 20), bg= "pink", width= 24, height= 2)
label.pack()

frame = Frame(root)
frame.pack()

button1 = Button(frame, text= 1, height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons(1))
button1.grid(row= 0, column= 0)

button2 = Button(frame, text= 2, height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons(2))
button2.grid(row= 0, column= 1)

button3 = Button(frame, text= 3, height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons(3))
button3.grid(row= 0, column= 2)

button4 = Button(frame, text= 4, height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons(4))
button4.grid(row= 1, column= 0)

button5 = Button(frame, text= 5, height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons(5))
button5.grid(row= 1, column= 1)

button6 = Button(frame, text= 6, height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons(6))
button6.grid(row= 1, column= 2)

button7 = Button(frame, text= 7, height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons(7))
button7.grid(row= 2, column= 0)

button8 = Button(frame, text= 8, height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons(8))
button8.grid(row= 2, column= 1)

button9 = Button(frame, text= 9, height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons(9))
button9.grid(row= 2, column= 2)

button0 = Button(frame, text= 0, height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons(0))
button0.grid(row= 3, column= 0)

buttonplus = Button(frame, text= "+", height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons("+"))
buttonplus.grid(row= 0, column= 3)

buttonminus = Button(frame, text= "-", height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons("-"))
buttonminus.grid(row= 1, column= 3)

buttonmultiply = Button(frame, text= "*", height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons("*"))
buttonmultiply.grid(row= 2, column= 3)

buttondivide = Button(frame, text= "/", height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons("/"))
buttondivide.grid(row= 3, column= 2)

buttonequalsto = Button(frame, text= "=", height= 4, width= 9, font= 25, bg= "pink", command= equalsto)
buttonequalsto.grid(row= 3, column= 3)

buttondecimal = Button(frame, text= ".", height= 4, width= 9, font= 25, bg= "white", command= lambda: buttons("."))
buttondecimal.grid(row= 3, column= 1)

buttonclear = Button(root, text= "C", height= 3, width= 14, font= 25, bg= "pink", command= clear)
buttonclear.pack()



root.mainloop()
