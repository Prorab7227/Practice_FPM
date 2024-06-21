import tkinter as tkk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

fig = Figure(figsize=(8, 5))
ax = fig.add_subplot(111)
canvas = None
toolbar = None

all_data = []

def File_select(file_output_entry: tkk.Entry):
    output_file_path = filedialog.askopenfilename()
    file_output_entry.delete(0, 'end')
    file_output_entry.insert(0, f'{output_file_path}')
    if output_file_path:
        with open(output_file_path, 'r') as f:
            x, y = [], []
            for string in f:
                string = string.split()
                x.append(float(string[0]))
                y.append(float(string[1]))
        return x, y, output_file_path
    else:
        file_output_entry.delete(0, 'end')
        file_output_entry.insert(0, 'Path')
        return [], [], ''

def Draw(file_output_entry: tkk.Entry, ox_move_entry: tkk.Entry, oy_move_entry: tkk.Entry, root: tkk.Tk, graph_listbox: tkk.Listbox):
    global fig, ax, canvas, toolbar, all_data

    x, y, file_path = File_select(file_output_entry)
    if not x or not y:
        return

    ox = float(ox_move_entry.get())
    oy = float(oy_move_entry.get())

    x = [float(xi) + ox for xi in x]
    y = [float(yi) + oy for yi in y]

    file_name = file_path.split('/')[-1]

    existing_items = graph_listbox.get(0, 'end')
    if file_name in existing_items:
        index = existing_items.index(file_name)
        del all_data[index]
        graph_listbox.delete(index)

    all_data.append((x, y, file_name))
    ax.cla()

    for data in all_data:
        ax.plot(data[0], data[1], label=data[2])

    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.legend()

    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

    if canvas is None:
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3, column=0, columnspan=3, pady=10)

        toolbar_frame = tkk.Frame(root)
        toolbar_frame.grid(row=4, column=0, columnspan=3, pady=10)
        toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
        toolbar.update()
    else:
        canvas.draw()

    graph_listbox.insert('end', file_name)

def Remove(graph_listbox: tkk.Listbox):
    global fig, ax, canvas, all_data

    selected_index = graph_listbox.curselection()
    if not selected_index:
        return

    del all_data[selected_index[0]]
    graph_listbox.delete(selected_index)
    ax.cla()

    for data in all_data:
        ax.plot(data[0], data[1], label=data[2])

    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.legend()

    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

    if canvas is not None:
        canvas.draw()
