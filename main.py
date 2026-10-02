from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Maths Table")

def generate():
    table = ""
    num = theNum.get()
    value = endVal.get()

    for i in range(value + 1):
        table += str(num)+ " X " + str(i) + " = " + str(num*i) + "\n"
    answer.config(text = table)
titl = Label(root, text = "Mathematical Table")
titl.grid(row = 0, column = 0, columnspan = 3, pady = 20)

nAndR = Label(root, text = "Number and Range:")
nAndR.grid(row = 1, column = 0, padx = 10)

theNum = IntVar()

numbers = Combobox(root, textvariable = theNum, width = 5)
numbers["values"] = tuple(range(101))

numbers.grid(row = 1, column = 1)

endVal = IntVar()
r10 = Radiobutton(root, text = "10", variable = endVal, value = 10)
r10.grid(row = 1, column = 2, padx = 30)

r20 = Radiobutton(root, text = "20", variable = endVal, value = 20)
r20.grid(row = 2, column = 2, padx = 30)

r30 = Radiobutton(root, text = "30", variable = endVal, value = 30)
r30.grid(row = 3, column = 2, padx = 30)

gen = Button(root, text = "Generate", command = generate)
gen.grid(row = 4, column = 1)

answer = Label(root)
answer.grid(row = 5, column = 1)

root.mainloop()