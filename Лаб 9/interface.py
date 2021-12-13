import tkinter as tk
from numpy import *
import matplotlib.pylab as plt

import table as tb

# Main window
window = tk.Tk()
window.title('Головне меню')

# Callbacks
def func1():
    table = tb.combine_tables()
    
    x = []
    y = []
    legends = []
    flag = True
    
    for row in table:
        if len(legends) == 0 or row[0] != legends[len(legends) - 1]:
            legends.append(row[0])
            y.append([])
            if len(x) != 0:
                flag = False
        if flag:
            x.append(int(row[1]))
        y[len(y) - 1].append(int(row[2]))
    
    for i in range(len(y)):
        plt.plot(x, y[i], label = legends[i])
    
    plt.xticks(x)
    plt.legend()

    plt.show()

def func2():
    table_window = tk.Toplevel(window)
    table_window.title('Таблиця')

    table = tb.combine_tables()
    
    headers = [
        'Найменування товарної групи',
        'Рік',
        'План',
        'Очікуєме виконання',
        'Торгова скидка, %'
    ]
    
    widths = [27, 4, 4, 18, 17]
    
    for i in range(len(headers)):
        tk.Label(table_window, text = headers[i], width = widths[i], height = 2, borderwidth = 2).grid(row = 0, column = i)
    
    for y in range(len(table)):
        for x in range(len(table[0])):
            tk.Label(table_window, text = table[y][x], width = widths[x], height = 2, borderwidth = 2).grid(row = y + 1, column = x)
    
    table_window.mainloop()

# Main Frame
frame = tk.Frame(master = window, borderwidth = 8)

button1 = tk.Button(frame, text = 'Відкрити графік', width = 25, height = 2, borderwidth = 2, command = func1)
button2 = tk.Button(frame, text = 'Відкрити таблицю', width = 25, height = 2, borderwidth = 2, command = func2)
button3 = tk.Button(frame, text = 'Експортувати в форматі JSON', width = 25, height = 2, borderwidth = 2, command = tb.make_json)
button4 = tk.Button(frame, text = 'Експортувати в форматі TXT', width = 25, height = 2, borderwidth = 2, command = tb.make_txt)

button1.pack(padx = 6, pady = 6)
button2.pack(padx = 6, pady = 6)
button3.pack(padx = 6, pady = 6)
button4.pack(padx = 6, pady = 6)

frame.pack()

window.mainloop()