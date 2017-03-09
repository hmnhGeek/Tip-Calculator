''' An app to find tips. '''

from Tkinter import *
import ttk

root = Tk()
root.geometry("550x400")
root.config(background = 'yellow')
root.resizable(height = 0, width = 0)
root.title("Tip Calculator")
var = IntVar()
# Define some labels now.

descriptor = Label(root, text = "Tip Calculator", font = ('timesnewroman', 20), bg = 'yellow', fg = "red")
descriptor.pack(pady = 20)

BILL_Label = Label(root, text = "BILL $: ", bg = 'yellow', fg = "red")
BILL_Label.pack(pady = 5)
BILL_Label.place(x = 110, y = 80)

BILL = ttk.Entry(root)
BILL.pack(pady = 5)
BILL.insert(END, "1000")

percents = [0.1, 0.15, 0.2]

def tip_percent():
    if var.get() <> 0:
        return var.get()*100**(-1)
    else:
        tip_label['text'] = "Please select a tip percentage."

def calc_tip():
    try:
        bill = float(BILL.get())
        tip_percentage = tip_percent()
        tip = bill*tip_percentage
        tip_label['text'] = "Tip $: "+str(round(tip, 2))+"\n"+"Total $: "+str(round(bill + tip, 2))
    except ValueError:
        tip_label['text'] = "The entered bill is not in correct format. -r integer."
    except TypeError:
        pass
    

for i in percents:
    Rb = Radiobutton(root, text = str(i*100)+'%', value = i*100, command = tip_percent, variable = var, bg = 'yellow',
                     activebackground = 'yellow', fg = "red", activeforeground = 'blue')
    Rb.pack(pady = 5)

b = ttk.Button(root, text = "Submit", command = calc_tip)
b.pack(pady = 10)

tip_label = Label(root, text = '', bg = 'yellow', font = ("consolas", 15), fg = "green")
tip_label.pack(pady = 5)

root.mainloop()
