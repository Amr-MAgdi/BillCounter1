import csv
import time
from tkinter import *
from tkinter import messagebox
import window as m
import pandas as pd


def times():
    current_time = time.strftime("Time: " + " %H:%M:%S \n" + "Date: " + " %d/%m/%Y \n" + "%A")
    m.label9.config(text=current_time)
    m.label9.after(1000, times)


def one():
    m.bill_1.insert(0, str(1))


def five():
    m.bill_more_1.delete(0, END)
    m.bill_more_1.insert(0, '')
    m.bill_more_1.insert(0, "5")


def ten():
    m.bill_more_1.delete(0, END)
    m.bill_more_1.insert(0, '')
    m.bill_more_1.insert(0, "10")


def twenty():
    m.bill_more_1.delete(0, END)
    m.bill_more_1.insert(0, '')
    m.bill_more_1.insert(0, "20")


def fifty():
    m.bill_more_1.delete(0, END)
    m.bill_more_1.insert(0, '')
    m.bill_more_1.insert(0, "50")


def one_hundred():
    m.bill_more_1.delete(0, END)
    m.bill_more_1.insert(0, '')
    m.bill_more_1.insert(0, "100")


def on_entry_click(event):
    # Function to handle the click event on the entry widget
    if m.bag_number.get() == 'Enter the bag number':
        m.bag_number.delete(0, END)
        m.bag_number.insert(0, '')


def save():
    bag_number = m.bag_number.get()
    bill = m.bill_1.get()
    Large_bill = m.bill_more_1.get()
    if m.number <= 2:
        df = pd.DataFrame.from_dict({"Bag ": [bag_number], "1$": [bill], "Large": [Large_bill]})
        df.to_csv(bag_number + ".csv", index=False, encoding='utf-8')
        with open("test.csv","a",) as file:
            myfile = csv.writer(file)
            bag = bag_number
            one = bill
            more = Large_bill
            myfile.writerow([bag, one, more])

    add_entry_value()


def calculate_sum():
    total = sum(map(float, entry_values))
    m.amount.config(text=f" {total:.2f}")


def add_entry_value():
    m.bill_1.insert(0, 0)
    entry_value = m.bill_1.get()
    bill = m.bill_more_1.get()
    try:
        if entry_value:
            if m.number <= 2:
                m.number += 1
                m.cash_box.config(text=str(m.number))
                entry_values.append(float(entry_value))
                entry_values.append(float(bill))
                m.bill_more_1.delete(0, END)
                m.bill_1.delete(0, END)
                calculate_sum()
            else:
                messagebox.showinfo("Error", "Please empty cashbox")
            m.last_bag_number.config(text=f"{float(entry_value) + float(bill):.2f}")
            m.bag_number.delete(0, END)
    except ValueError:
        messagebox.showinfo("Error", "Please Enter a bill")


entry_values = []


def empty_box():
    m.amount.config(text="0")

# google_sheet()
