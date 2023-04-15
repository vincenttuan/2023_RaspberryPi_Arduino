'''
GUI
+------+------+------+------+
| 溫度 | 25 C | 濕度  | 53 % |
+------+------+------+------+
|    Data    |      77      |
+------+------+------+------+
| LED1 | LED2 | LED3 | LED3 |
+------+------+------+------+
'''

import tkinter
import threading
from tkinter import font

if __name__ == '__main__':

    win = tkinter.Tk()
    win.title('Smart House')
    win.geometry('700x500')

    myfont = font.Font(family='Arial', size=24, weight='bold')

    temp_value = tkinter.StringVar()
    temp_value.set('0°C')
    humd_value = tkinter.StringVar()
    humd_value.set('0%')
    data_value = tkinter.StringVar()
    data_value.set('0')
    # view 元件
    temp_label = tkinter.Label(text='溫度', font=myfont)
    humd_label = tkinter.Label(text='濕度', font=myfont)
    temp_value_label = tkinter.Label(textvariable=temp_value, font=myfont)
    humd_value_label = tkinter.Label(textvariable=humd_value, font=myfont)
    data_label = tkinter.Label(text='Data', font=myfont)
    data_value_label = tkinter.Label(textvariable=data_value, font=myfont)
    led1_button = tkinter.Button(text='LED1', font=myfont)
    led2_button = tkinter.Button(text='LED2', font=myfont)
    led3_button = tkinter.Button(text='LED3', font=myfont)
    led4_button = tkinter.Button(text='LED4', font=myfont)

    win.rowconfigure((0, 1, 2), weight=1)  # 列 0, 1, 2 同步放大與縮小
    win.columnconfigure((0, 1, 2, 3), weight=1)  # 欄 0, 1, 2, 3 同步放大與縮小

    # 將 view 元件配置到 grid 元件中
    # 第一列
    temp_label.grid(row=0, column=0, sticky='EWNS')
    temp_value_label.grid(row=0, column=1, sticky='EWNS')
    humd_label.grid(row=0, column=2, sticky='EWNS')
    humd_value_label.grid(row=0, column=3, sticky='EWNS')
    # 第二列
    data_label.grid(row=1, column=0, columnspan=2, sticky='EWNS')
    data_value_label.grid(row=1, column=2, columnspan=2, sticky='EWNS')
    # 第三列
    led1_button.grid(row=2, column=0, sticky='EWNS')
    led2_button.grid(row=2, column=1, sticky='EWNS')
    led3_button.grid(row=2, column=2, sticky='EWNS')
    led4_button.grid(row=2, column=3, sticky='EWNS')

    win.mainloop()







