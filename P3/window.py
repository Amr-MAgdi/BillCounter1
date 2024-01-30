from tkinter import *

import main as f



# #########################################################################################################
root = Tk()


root.title("Bill Calculator")
root.geometry("700x900")
# ############################################################################################################################

label1 = Label(root,
               text="Vend Special Bill Calculator",
               fg="black",
               font=("Helvetica", 20, "bold"),
               background="#ABB3DE",
               border=15)
label1.pack(padx=10, pady=10)
# ############################################################################################################################

frame1 = Frame(root, width=700, height=70)
label2 = Label(frame1, font=("Helvetica", 16),
               text="Bag: ",
               background="gray",
               border=5,
               foreground="black")
label2.pack(side=LEFT, padx=5, pady=5)
bag_number = Entry(frame1, font=("Helvetica", 16),
                   background="white",
                   border=5,
                   foreground="black",
                   )
bag_number.insert(0, 'Enter the bag number')

bag_number.pack(side=RIGHT)

bag_number.bind("<FocusIn>", f.on_entry_click)

frame1.pack()
# ############################################################################################################################
frame2 = Frame(root, width=700, height=70)
label3 = Label(frame2, font=("Helvetica", 16),
               text="$1s: ",
               background="gray",
               border=5,
               foreground="black")
label3.pack(side=LEFT, padx=5, pady=5)
bill_1 = Entry(frame2, font=("Helvetica", 16), background="white", border=5, foreground="black",)

bill_1.pack(side=RIGHT)

frame2.pack()
# ############################################################################################################################

frame3 = Frame(root, width=700, height=70)
label4 = Label(frame3, text="$larger: ",
               font=("Helvetica", 16),
               background="gray",
               border=5,
               foreground="black")
label4.pack(side=LEFT, padx=5, pady=5)
bill_more_1 = Entry(frame3, font=("Helvetica", 16), background="white", border=5, foreground="black",  )


bill_more_1.pack(side=RIGHT)

frame3.pack()
# ############################################################################################################################

frame4 = Frame(root, width=700, height=70)
button1 = Button(frame4, text="$1",
                 font=("Helvetica", 16),
                 background="gray",
                 border=5,
                 foreground="black",
                 command=f.one
                 )

button1.pack()
button2 = Button(frame4, text="$5",
                 font=("Helvetica", 16),
                 background="gray",
                 border=5,
                 foreground="black",
                 command=f.five
                 )
button2.pack()
button3 = Button(frame4, text="$10",
                 font=("Helvetica", 16),
                 background="gray",
                 border=5,
                 foreground="black",
                 command=f.ten
                 )
button3.pack()
button4 = Button(frame4, text="$20",
                 font=("Helvetica", 16),
                 background="gray",
                 border=5,
                 foreground="black",
                 command=f.twenty
                 )
button4.pack()
button5 = Button(frame4, text="$50",
                 font=("Helvetica", 16),
                 background="gray",
                 border=5,
                 foreground="black",
                 command=f.fifty
                 )
button5.pack()

button6 = Button(frame4, text="$100",
                 font=("Helvetica", 16),
                 background="gray",
                 border=5,
                 foreground="black",
                 command=f.one_hundred
                 )
button6.pack()

frame4.pack()
# ############################################################################################################################

frame5 = Frame(root, width=700, height=70)
label5 = Label(frame5, text="$Last Bill : ",
               font=("Helvetica", 16),
               background="gray",
               border=5,
               foreground="black")
label5.pack(side=LEFT, padx=5, pady=5)
last_bag_number = Label(frame5, text="0", font=("Helvetica", 16), background="white", border=5, foreground="black")
last_bag_number.pack(side=RIGHT)

frame5.pack()
# ############################################################################################################################

button7 = Button(root,
                 text="Close Bag",
                 font=("Helvetica", 16),
                 background="gray",
                 border=5,
                 foreground="black",
                 command=f.save,
                 )
button7.pack()

# ############################################################################################################################

frame6 = Frame(root, width=700)
label6 = Label(frame6, text="CashBox Bill : ",
               font=("Helvetica", 16),
               background="gray",
               border=5,
               foreground="black")
label6.pack(side=LEFT, padx=5, pady=5)
number = 0
cash_box = Label(frame6, text=str(number), font=("Helvetica", 16), background="white", border=5, foreground="black")
cash_box.pack(side=RIGHT)

frame6.pack()
# ############################################################################################################################

frame7 = Frame(root, width=700)
label7 = Label(frame7, text="CashBox Amount : ",
               font=("Helvetica", 16),
               background="gray",
               border=5,
               foreground="black")
label7.pack(side=LEFT, padx=5, pady=5)
Amount = 0
amount = Label(frame7, text=str(Amount), font=("Helvetica", 16), background="white", border=5, foreground="black")
amount.pack(side=RIGHT)
frame7.pack()
# ############################################################################################################################

button8 = Button(root,
                 text="Empty CashBox",
                 font=("Helvetica", 16),
                 background="gray",
                 border=5,
                 foreground="black",
                 command=f.empty_box)
button8.pack()
# ############################################################################################################################

frame8 = Frame(root, width=700, )
label8 = Label(frame8, text="Time : ",
               font=("Helvetica", 16),
               background="gray",
               border=5,
               foreground="black")
label8.pack(side=LEFT, padx=5, pady=5)
label9 = Label(frame8, font=("Helvetica", 16), background="white", border=5, foreground="black")
label9.pack(side=RIGHT)
f.times()
frame8.pack()

# ############################################################################################################################

root.mainloop()
