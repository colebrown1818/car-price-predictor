# Import Module
import pandas as pd
from tkinter import *
# import sklearn as sci
import pickle


# create root window
root = Tk()

# root window title and dimension
root.title("Tacoma Price Predicter")
# Set geometry (width x height)
root.geometry('350x200')

# adding menu bar in root window
# new item in menu bar labeled as 'New
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# adding a label to the root window
def label_entry(text, row):
    lbl = Label(root, text = text)
    lbl.grid()

    # adding Entry Field
    txt = Entry(root, width=10)
    txt.grid(column=1, row=row)

    return lbl, txt

lbl, txt = label_entry(text='Mileage', row=0)

lbl2, txt2 = label_entry(text='Cylinders', row=1)

lbl3, txt3 = label_entry(text='Days on the Market', row=2)

lbl4, txt4 = label_entry(text='Model Year', row=3)

trims = ['Limited', 'Limited HV', 'PreRunner V6', 'SR', 'SR V6', 'SR5', 'SR5 V6', 'TRD Off-Road', 'TRD PreRunner', 'TRD Pro', 'TRD Pro HV', 'TRD Sport', 'TRD Sport HV', 'Trailhunter HV', 'V6']

trim_select = StringVar(root)
trim_select.set("Select a Trim")

# Create the dropdown menu
dropdown = OptionMenu(root, trim_select, *trims)
dropdown.grid(column=0, row=4)

drivelines = ['4x4','RWD']

driveline_select = StringVar(root)
driveline_select.set("Select a Driveline")

# Create the dropdown menu
dropdown = OptionMenu(root, driveline_select, *drivelines)
dropdown.grid(column=0, row=5)

transmissions = ['automatic','manual']

transmission_select = StringVar(root)
transmission_select.set("Select a Transmission")

# Create the dropdown menu
dropdown = OptionMenu(root, transmission_select, *transmissions)
dropdown.grid(column=0, row=6)

data = {}
def clicked():
    data['mileage'] = float(txt.get())
    data['cylinder'] = float(txt2.get())
    data['daysOnMarket'] = int(txt3.get())
    data['year_old'] = 2024 - int(txt4.get())
    data['model_toyota_tacoma'] = 1

    trim = trim_select.get()

    for i in trims:
        trim_label = 'trim_' + i
        if i == trim:
            data[trim_label] = 1
        else:
            data[trim_label] = 0

    driveline = driveline_select.get()

    for i in drivelines:
        driveline_label = 'driveline_' + i
        if i == driveline:
            data[driveline_label] = 1
        else:
            data[driveline_label] = 0
    
    transmission = transmission_select.get()

    for i in transmissions:
        transmission_label = 'transmission_' + i
        if i == transmission:
            data[transmission_label] = 1
        else:
            data[transmission_label] = 0
    
    df = pd.DataFrame(data,index=[0])
    df.to_csv('test_predict.csv')
    
    with open('xgboost_tuned.pkl','rb') as f:
        model = pickle.load(f)

    y_prediction = model.predict(df)

    for widget in root.winfo_children():
        widget.destroy()
    
    lbl = Label(root, text = 'This vehcile should cost: $' + "{:,.0f}".format(y_prediction[0]))
    lbl.grid()

    
# button widget with red color text inside
btn = Button(root, text = 'Calculate', fg="red", command=clicked)

# set Button grid
btn.grid(column=3, row=6,sticky=SE)

# all widgets will be here
# Execute Tkinter
root.mainloop()
