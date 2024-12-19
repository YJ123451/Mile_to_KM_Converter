from tkinter import *
window = Tk()
window.title("Mile to KM Converter")
window.config(padx = 20,pady=20)


def convert():
    km  = float(input.get()) * 1.609
    label3.config(text=f"{km}")


# Label 1
label1 = Label(text= "Miles")
label1.grid(column = 2, row = 0)

#Label 2
label2 = Label(text = "is equal to")
label2.grid(column = 0, row = 1)

#Label 3
label3 = Label(text = "0")
label3.grid(column = 1, row = 1)

#Label 4
label4 = Label(text = "Km")
label4.grid(column = 2, row = 1)

#Entry
input = Entry(width=7)
input.insert(END,string = "0")
input.grid(column = 1,row = 0)

# Button
button = Button(text="Calculate",command=convert)
button.grid(column =1, row = 2)















window.mainloop()