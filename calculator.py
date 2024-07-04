from tkinter import *

label_str = []
previous_value = 0
data = []
operators = ['+', '-', '/', 'X', '%']


def click(e):
    global label_str, data, previous_value
    if e in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '.', '%', '+', '-', '/', 'X']:
        if isinstance(e, int) and previous_value != 0 and len(data) == 0:
            new_operation()
        label_str.append(e)
        l_eq.config(text=create_output_string(label_str))
        data.append(e)
    elif e == 'Del':
        delete()
    elif e == 'C':
        clear()
    elif e == '=':
        equals()


def new_operation():
    global previous_value, label_str, l_eq
    label_str.clear()
    l_eq.config(text="")
    previous_value = 0


def create_output_string(elements):
    string = ""
    for char in elements:
        if isinstance(char, int):
            string += f"{char}"
        else:
            string += f" {char} "
    return string


def delete():
    global label_str, data, l_eq
    if len(data) > 0:
        del label_str[len(label_str) - 1]
        del data[len(data) - 1]
        l_eq.config(text=create_output_string(label_str))


def clear():
    global previous_value, label_str, data
    previous_value = 0
    entity.delete(0, END)
    label_str.clear()
    l_eq.config(text="")
    data.clear()
    entity.delete(0, END)
    l_eq.config(text='')


def equals():
    global data
    entity.delete(0, END)
    entity.insert(0, operate(data))
    label_str.clear()
    label_str.append(previous_value)
    l_eq.config(text=create_output_string(label_str))
    data.clear()


def operate(data):
    global label_str, operators
    try:
        if len(data) == 0:
            return previous_value
        if len(data) == 1 or not contains_operator(data):
            return 'Error'
        if data[0] in operators:
            first_number = previous_value
            second_number, index = create_digit(data, 1)
            calculate(first_number, data[0], second_number)
            if index == 0:
                return previous_value
            if index < len(data) - 1:
                new_data = data[index:]
                operate(new_data)
        else:

            first_number, index = create_digit(data, 0)
            if index < len(data) - 1:
                second_number, val = create_digit(data, index + 1)
                operator = data[index]
                calculate(first_number, operator, second_number)
                if val == 0:
                    return previous_value
                else:
                    if index < len(data) - 1:
                        new_data = data[index:]
                        operate(new_data)
            else:
                return 'Error'
        return previous_value
    except Exception as e:
        return 'Error'


def contains_operator(data):
    flag = False
    for item in data:
        if item in ['+', '-', '/', 'X', '%']:
            flag = True
            return flag
    return flag


def create_digit(data, i):
    dot = False
    number = 0
    while i < len(data):
        if data[i] != '.' and data[i] not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
            return number, i
        if data[i] == '.':
            dot = True
            i += 1
            continue
        if dot:
            number += data[i] / 10
        else:
            number = number * 10 + data[i]
        i += 1
    return number, 0


def calculate(first_number, operator, second_number):
    global previous_value
    if operator == '+':
        previous_value = first_number + second_number
    elif operator == 'X':
        previous_value = first_number * second_number
    elif operator == '-':
        previous_value = first_number - second_number
    elif operator == '/':
        previous_value = first_number / second_number
    elif operator == '%':
        previous_value = first_number % second_number


# GUI Code
root = Tk()
root.title("Calculater")
root.config(bg="white")
root.geometry("300x400")
root.iconbitmap("./icon.ico")
l_eq = Label(root, width=30, bg='white', fg='teal', font=('arial', 13, 'bold'), anchor='w')

l_eq.grid(row=0, columnspan=4, pady=(50, 0))
entity = Entry(root, width=20, border=0, font=('arial', 20))
entity.grid(row=1, columnspan=4, pady=(10, 5))


def on_enter(e):
    if e.widget['text'] in ["+", "X", "-", "/"]:
        e.widget['background'] = equal_color
    elif e.widget['text'] == "=":
        e.widget['background'] = equal_hover_color
    else:
        e.widget['background'] = sub_color


def on_leave(e):
    if e.widget['text'] in ["X", "-", "/", "+"]:
        e.widget['background'] = sub_color
    elif e.widget['text'] == "=":
        e.widget['background'] = equal_color
    else:
        e.widget['background'] = main_color


def create_button(text, width, height, bg_color, font, active_color, border, command, grid):
    global default_fg
    fg = default_fg
    if text == '=':
        fg = 'white'
    button = Button(root, text=text, width=width, height=height, bg=bg_color, fg=fg, font=font,
                    activebackground=active_color, borderwidth=border, command=command)
    button.grid(row=grid[0], column=grid[1], pady=grid[2], columnspan=grid[3], sticky=grid[4])
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    return button


# Create buttons
default_fg = "SystemButtonText"
main_color = "#E0E0E0"
sub_color = "#b3e0dc"
equal_color = "teal"
equal_hover_color = "#26A69A"
buttons = [
    ('C', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click("C"), (2, 0, 2, 1, '')),
    ('%', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click("%"), (2, 1, 2, 1, '')),
    ('Del', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click("Del"), (2, 2, 2, 1, '')),
    ('+', 4, 1, sub_color, ('arial', 20), sub_color, .3, lambda: click("+"), (2, 3, 2, 1, '')),
    ('1', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click(1), (3, 0, 2, 1, '')),
    ('2', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click(2), (3, 1, 2, 1, '')),
    ('3', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click(3), (3, 2, 2, 1, '')),
    ('-', 4, 1, sub_color, ('arial', 20), sub_color, .3, lambda: click("-"), (3, 3, 2, 1, '')),
    ('4', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click(4), (4, 0, 2, 1, '')),
    ('5', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click(5), (4, 1, 2, 1, '')),
    ('6', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click(6), (4, 2, 2, 1, '')),
    ('X', 4, 1, sub_color, ('arial', 20), main_color, .3, lambda: click("X"), (4, 3, 2, 1, '')),
    ('7', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click(7), (5, 0, 2, 1, '')),
    ('8', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click(8), (5, 1, 2, 1, '')),
    ('9', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click(9), (5, 2, 2, 1, '')),
    ('/', 4, 1, sub_color, ('arial', 20), sub_color, .3, lambda: click("/"), (5, 3, 2, 1, '')),
    ('0', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click(0), (6, 0, 2, 1, '')),
    ('.', 4, 1, main_color, ('arial', 20), main_color, .3, lambda: click("."), (6, 1, 2, 1, '')),
    ('=', 4, 1, equal_color, ('arial', 20), equal_color, .3, lambda: click("="), (6, 2, 2, 2, 'EW')),
]

for text, width, height, bg_color, font, active_color, border, command, grid in buttons:
    create_button(text, width, height, bg_color, font, active_color, border, command, grid)

root.mainloop()
