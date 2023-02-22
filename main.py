from tkinter import *
from math import cos, sin, pi, prod, pow, factorial, sqrt
from re import subn


def remove_text_between_parens(text):
    return text.replace('(', '').replace(')', '')


def add_digit(digit):
    label = calc.get()
    if "π" == digit:
        digit = str(round(pi, 2))
        value = multiply(label + "*" + digit)
    elif "±" == digit:
        if label.startswith("-"):
            value = label.replace("-", "")
        else:
            value = "-" + label
    elif "n!" == digit:
        try:
            value = str(factorial(int(label)))
        except ValueError:
            index_search = label.index(".")
            label = label[:index_search]
            value = str(factorial(int(label)))
    elif "√" == digit:
        value = num_root(label)
    else:
        value = label + str(digit)
    calc.delete(0, END)
    calc.insert(0, value)


def equals():
    value = calc.get()
    calc.delete(0, END)
    answer = '0'
    if "+" in value:
        answer = plus(value)
    elif "-" in value:
        answer = minus(value)
    elif "*" in value:
        answer = multiply(value)
    elif "/" in value:
        answer = division(value)
    elif "xⁿ" in value:
        answer = degree(value)
    elif 'sin' in value:
        value = value.replace('sin', '')
        answer = remove_text_between_parens(str(sin(int(value))))
    elif 'cos' in value:
        value = value.replace('cos', '')
        answer = remove_text_between_parens(str(cos(int(value))))

    calc.insert(0, answer)


def plus(value):
    try:
        value_list = list(map(int, value.split("+")))
    except ValueError:
        value_list = list(map(float, value.split("+")))
    return str(sum(value_list))


def division(value):
    try:
        value_list = list(map(int, value.split("/")))
    except ValueError:
        value_list = list(map(float, value.split("/")))
    return remove_text_between_parens(str(divmod(value_list[0], prod(value_list[1:]))))


def multiply(value):
    try:
        value_list = list(map(int, value.split("*")))
    except ValueError:
        value_list = list(map(float, value.split("*")))
    return str(prod(value_list))


def minus(value):
    value_list = [int(i) for i in value.split("-")]
    first_num = value_list[0]
    last_num = sum(list(map(int, value_list[1:])))
    return str(first_num - last_num)


def degree(value):
    try:
        value_list = list(map(int, value.split("xⁿ")))
    except ValueError:
        value_list = list(map(float, value.split("xⁿ")))
    if len(value_list) == 2:
        answer = str(pow(value_list[0], value_list[1]))
    else:
        raise IndexError
    return answer


def delete_digit():
    calc.delete(0, END)


def exit_digit():
    calc.quit()


def num_root(value):
    try:
        value = int(value)
    except ValueError:
        index_search = value.index(".")
        value = int(value[:index_search])
    value = str(sqrt(value))
    return value


root = Tk()
root.title("Calculator")
root.geometry(f"300x387+150+250")
root['bg'] = "#33ffe6"


calc = Entry(root, justify=RIGHT, font=("Arial", 15), width=15)
calc.grid(row=0, column=0, columnspan=5, sticky="we")

Button(text="7", bd=5, font=("Arial", 13), command=lambda: add_digit("7")).grid(row=1, column=0, sticky="wens")
Button(text="8", bd=5, font=("Arial", 13), command=lambda: add_digit("8")).grid(row=1, column=1, sticky="wens")
Button(text="9", bd=5, font=("Arial", 13), command=lambda: add_digit("9")).grid(row=1, column=2, sticky="wens")
Button(text="+", bd=5, font=("Arial", 13), command=lambda: add_digit("+")).grid(row=1, column=3, sticky="wens")
Button(text="*", bd=5, font=("Arial", 13), command=lambda: add_digit("*")).grid(row=1, column=4, sticky="wens")

Button(text="4", bd=5, font=("Arial", 13), command=lambda: add_digit("4")).grid(row=2, column=0, sticky="wens")
Button(text="5", bd=5, font=("Arial", 13), command=lambda: add_digit("5")).grid(row=2, column=1, sticky="wens")
Button(text="6", bd=5, font=("Arial", 13), command=lambda: add_digit("6")).grid(row=2, column=2, sticky="wens")
Button(text="-", bd=5, font=("Arial", 13), command=lambda: add_digit("-")).grid(row=2, column=3, sticky="wens")
Button(text="/", bd=5, font=("Arial", 13), command=lambda: add_digit("/")).grid(row=2, column=4, sticky="wens")

Button(text="1", bd=5, font=("Arial", 13), command=lambda: add_digit("1")).grid(row=3, column=0, sticky="wens")
Button(text="2", bd=5, font=("Arial", 13), command=lambda: add_digit("2")).grid(row=3, column=1, sticky="wens")
Button(text="3", bd=5, font=("Arial", 13), command=lambda: add_digit("3")).grid(row=3, column=2, sticky="wens")
Button(text="=", bd=5, font=("Arial", 13), command=lambda: equals()).grid(row=3, column=3, sticky="wens")
Button(text="xⁿ", bd=5, font=("Arial", 13), command=lambda: add_digit("xⁿ")).grid(row=3, column=4, sticky="wens")

Button(text="0", bd=5, font=("Arial", 13), command=lambda: add_digit("0")).grid(row=4, column=0, sticky="wens")
Button(text=".", bd=5, font=("Arial", 13), command=lambda: add_digit(".")).grid(row=4, column=1, sticky="wens")
Button(text="±", bd=5, font=("Arial", 13), command=lambda: add_digit("±")).grid(row=4, column=2, sticky="wens")
Button(text="C", bd=5, font=("Arial", 13), command=lambda: delete_digit()).grid(row=4, column=3, sticky="wens")

Button(text="Exit", bd=5, font=("Arial", 13), command=lambda: exit_digit()).grid(row=5, column=0, sticky="wens")
Button(text="π", bd=5, font=("Arial", 13), command=lambda: add_digit("π")).grid(row=5, column=1, sticky="wens")
Button(text="sin", bd=5, font=("Arial", 13), command=lambda: add_digit("sin")).grid(row=5, column=2, sticky="wens")
Button(text="cos", bd=5, font=("Arial", 13), command=lambda: add_digit("cos")).grid(row=5, column=3, sticky="wens")

Button(text="(", bd=5, font=("Arial", 13), command=lambda: add_digit("(")).grid(row=6, column=0, sticky="wens")
Button(text=")", bd=5, font=("Arial", 13), command=lambda: add_digit(")")).grid(row=6, column=1, sticky="wens")
Button(text="n!", bd=5, font=("Arial", 13), command=lambda: add_digit("n!")).grid(row=6, column=2, sticky="wens")
Button(text="√", bd=5, font=("Arial", 13), command=lambda: add_digit("√")).grid(row=6, column=3, sticky="wens")


root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)
root.grid_columnconfigure(4, minsize=60)

root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)
root.grid_rowconfigure(5, minsize=60)
root.grid_rowconfigure(6, minsize=60)

root.mainloop()
