import tkinter as tkk
from tkinter import Tk
from calculation import Main_calc
from draw import Draw, Remove

def fmain() -> None:
    root = Tk()
    root.title('Practice')

    button_width = 10

    # Frames
    upper_frame = tkk.Frame(root)
    upper_frame.grid(row=0, column=0, sticky='nsew', pady=10, padx=80)

    upper_frame.grid_columnconfigure(0, minsize=100)
    upper_frame.grid_columnconfigure(1, minsize=100)
    upper_frame.grid_columnconfigure(2, minsize=100)

    medium_frame = tkk.Frame(root)
    medium_frame.grid(row=1, column=0, sticky='nsew', pady=10, padx=20)

    medium_frame.grid_columnconfigure(0, minsize=100)
    medium_frame.grid_columnconfigure(1, minsize=100)
    medium_frame.grid_columnconfigure(2, minsize=100)

    # Calculation
    file_input_lab = tkk.Label(upper_frame, text='Output file')
    file_input_entry = tkk.Entry(upper_frame)
    file_input_entry.insert(0, 'File.txt')

    min_lab = tkk.Label(upper_frame, text='Min')
    min_ent = tkk.Entry(upper_frame)
    min_ent.insert(0, '0')

    max_lab = tkk.Label(upper_frame, text='Max')
    max_ent = tkk.Entry(upper_frame)
    max_ent.insert(0, '0')

    step_lab = tkk.Label(upper_frame, text='Step')
    step_ent = tkk.Entry(upper_frame)
    step_ent.insert(0, '0')

    prep_button = tkk.Button(upper_frame, text='Prepare', width=button_width, command=lambda:Main_calc(file_input_entry, min_ent, max_ent, step_ent))

    # Placing
    file_input_lab.grid(row=0, column=0)
    min_lab.grid(row=1, column=0)
    max_lab.grid(row=2, column=0)
    step_lab.grid(row=3, column=0)

    file_input_entry.grid(row=0, column=1)
    min_ent.grid(row=1, column=1)
    max_ent.grid(row=2, column=1)
    step_ent.grid(row=3, column=1)

    prep_button.grid(row=1, column=2)

    # Drawing
    file_output_lab = tkk.Label(medium_frame, text='Input file')
    file_output_entry = tkk.Entry(medium_frame, width=40)
    file_output_entry.insert(0, 'Path')

    ox_move_lab = tkk.Label(medium_frame, text='OX')
    ox_move_entry = tkk.Entry(medium_frame, width=40)
    ox_move_entry.insert(0, '0')

    oy_move_lab = tkk.Label(medium_frame, text='OY')
    oy_move_entry = tkk.Entry(medium_frame, width=40)
    oy_move_entry.insert(0, '0')

    graph_listbox = tkk.Listbox(medium_frame, height=3, selectmode=tkk.SINGLE)
    draw_f = tkk.Button(medium_frame, text='Draw f(x)', width=button_width, command=lambda:Draw(file_output_entry, ox_move_entry, oy_move_entry, root, graph_listbox))

    remove_button = tkk.Button(medium_frame, text='Remove', width=button_width, command=lambda:Remove(graph_listbox))

    # Placing
    file_output_lab.grid(row=0, column=0)
    ox_move_lab.grid(row=1, column=0)
    oy_move_lab.grid(row=2, column=0)

    file_output_entry.grid(row=0, column=1)
    ox_move_entry.grid(row=1, column=1)
    oy_move_entry.grid(row=2, column=1)

    draw_f.grid(row=1, column=2)

    graph_listbox.grid(row=3, column=0, columnspan=2, pady=10)
    remove_button.grid(row=3, column=2)

    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    fmain()
