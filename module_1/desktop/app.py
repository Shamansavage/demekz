import tkinter as tk 
from mysql.connector import connect

import datetime 

app = tk.Tk()
app.geometry('500x500')

fio_label = tk.Label(app, text='ФИО клиента')
fio = tk.Entry(app, width='30')
fio_label.place(x=50, y=30)
fio.place(x=50, y=50)

namecomp_label = tk.Label(app, text='Название компании')
namecomp = tk.Entry(app, width='30')
namecomp_label.place(x=50, y=80)
namecomp.place(x=50, y=100)

services_label = tk.Label(app, text='Услуги')
services = tk.Entry(app, width='30')
services_label.place(x=50, y=130)
services.place(x=50, y=150)

id_lab = tk.Label(app, text='Код лабораторного сосуда')
id = tk.Entry(app, width='30')
id_lab.place(x=50, y=180)
id.place(x=50, y=200)

price_lab = tk.Label(app, text='Цена')
price =  tk.Entry(app, width='30')
price_lab.place(x=50, y=230)
price.place(x=50, y=250)


submit = tk.Button(app,text='Формирование заказа', width='30', height='5')
submit.place(x=125, y=280)

app.mainloop()