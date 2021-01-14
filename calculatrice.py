import tkinter as tk

window = tk.Tk()
ent_input = tk.Entry()
history = []

def insertNum(num):
    ent_input.insert(tk.END, f"{num}")

def historyToString(history):
    string = ""
    for calc in history:
        string += f"{calc[1] + '=>' + calc[2]}"
    return string

num_pad = tk.Frame(
    master = window
)

operation_pad = tk.Frame(
    master = window
)

history_log = tk.Button(
    master = window,
    text = historyToString(history)
)

def historise(calc):
    print(calc)
    print(history)
    history.append(calc)

def generateNumPad(maxnum):
    for i in range(maxnum):
        btn = tk.Button(
            master = num_pad,
            text = f"{i}",
            width = 10,
            height = 5,
            command = lambda: insertNum(f"{i}")
        )
        btn.pack()

def clear():
    ent_input.delete(0, tk.END)

def calc(calc):
    result = eval(calc)
    ent_input.delete(0, tk.END)
    ent_input.insert(0, result)
    historise([calc, result])

btn0 = tk.Button(
     master = num_pad,
    text = "0",
    width = 10,
    height = 5,
    command = lambda: insertNum("0")
)
btn1 = tk.Button(
     master = num_pad,
    text = "1",
    width = 10,
    height = 5,
    command = lambda: insertNum("1")
)
btn2 = tk.Button(
     master = num_pad,
    text = "2",
    width = 10,
    height = 5,
    command = lambda: insertNum("2")
)
btn3 = tk.Button(
     master = num_pad,
    text = "3",
    width = 10,
    height = 5,
    command = lambda: insertNum("3")
)
btn4 = tk.Button(
     master = num_pad,
    text = "4",
    width = 10,
    height = 5,
    command = lambda: insertNum("4")
)
btn5 = tk.Button(
     master = num_pad,
    text = "5",
    width = 10,
    height = 5,
    command = lambda: insertNum("5")
)
btn6 = tk.Button(
     master = num_pad,
    text = "6",
    width = 10,
    height = 5,
    command = lambda: insertNum("6")
)
btn7 = tk.Button(
     master = num_pad,
    text = "7",
    width = 10,
    height = 5,
    command = lambda: insertNum("7")
)
btn8 = tk.Button(
     master = num_pad,
    text = "8",
    width = 10,
    height = 5,
    command = lambda: insertNum("8")
)
btn9 = tk.Button(
     master = num_pad,
    text = "9",
    width = 10,
    height = 5,
    command = lambda: insertNum("9")
)
btn_clear = tk.Button(
    master = operation_pad,
    text = "C",
    width = 10,
    height = 5,
    command = lambda: clear()
)
btn_plus = tk.Button(
    master = operation_pad,
    text = "+",
    width = 10,
    height = 5,
    command = lambda: insertNum("+")
)
btn_minus = tk.Button(
    master = operation_pad,
    text = "-",
    width = 10,
    height = 5,
    command = lambda: insertNum("-")
)
btn_times = tk.Button(
    master = operation_pad,
    text = "x",
    width = 10,
    height = 5,
    command = lambda: insertNum("*")
)
btn_divide = tk.Button(
    master = operation_pad,
    text = "/",
    width = 10,
    height = 5,
    command = lambda: insertNum("/")
)
btn_equal = tk.Button(
    master = operation_pad,
    text = "=",
    width = 10,
    height = 5,
    command = lambda: calc(ent_input.get())
)

ent_input.pack()
btn_clear.pack()
btn_plus.pack()
btn_minus.pack()
btn_times.pack()
btn_divide.pack()
btn_equal.pack()

btn0.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()
btn8.pack()
btn9.pack()

operation_pad.pack(
    side = tk.LEFT
)

num_pad.pack(
    fill = tk.X
)

history_log.pack(
    side = tk.RIGHT
    fill = tk.BOTH
)

window.mainloop()
