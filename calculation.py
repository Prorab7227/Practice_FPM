import math
from numpy import cbrt
import tkinter as tkk
from tkinter import messagebox, filedialog

input_file_name = ''

def F_calc(x:float) -> float:
    if(6<x<8):
        return float((cbrt(math.exp(-3+x))) / math.sqrt( (x**2) + (x**4) + math.log(abs(x-1.2) )))
    elif(-3<x<=0):
        if x == 0: return 0
        else: return float(x**(-6))
    else:
        return float((x**15)-2)

def Main_calc(file_input_entry:tkk.Entry, min_ent:tkk.Entry, max_ent:tkk.Entry, step_ent:tkk.Entry):
    global input_file_name
    input_file_name = str(file_input_entry.get())
    try:
        min_value = float(min_ent.get())
        max_value = float(max_ent.get())
        step_value = float(step_ent.get())
    except ValueError:
        messagebox.showwarning('Error', 'Min, max or step can`t be a str')
        return 0
    current_value = min_value
    x = []

    if min_value == max_value:
        messagebox.showwarning('Error','Min and Max, can`t be the same')
        return 0
    if step_value == 0:
        messagebox.showwarning('Error','Step can`t be equal 0')
        return 0
    if (max_value-min_value<step_value):
        messagebox.showwarning('Error','Step is to large')
        return 0

    while current_value <= max_value:
        x.append(current_value)
        current_value+=step_value
    
    y = [F_calc(i) for i in x]
    print(f'\n{x}\n{y}')
    Save_file(x,y)

def Save_file(x:list[float],y:list[float]):
    root_path = filedialog.askdirectory()
    data_path = f'{root_path}/{input_file_name}'
    with open(data_path, 'w') as f:
        for i in range(len(x)):
            f.write(f'{x[i]} {y[i]}\n')