try:
    import tkinter
except ImportError:
    import TKinter as tkinter

import os

# Rasheed_stuff = { "Rasheed": "He is the best", "Collin": "He is the worst", "Ava": "She is the cutests"
# }


mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('1040x480+8+400')
mainWindow['padx'] = 8

# Adding a label to the grid

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

# The styling of the rows and columns
mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

# Creating the List Box
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
# Filling the List Box with data
for zone in os.listdir('/Windows/System32'):
    fileList.insert(tkinter.END, zone)

# Rasheed's example
# for i in Rasheed_stuff.keys():
#     fileList.insert(tkinter.END, i)


# Adding the Scroll Bar to the List Box
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# frame for the radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
# Setting the default value of the radio buttons
rbValue.set(3)
# Radio Buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# Creating a label
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')

# Data Entry Box, More like a data field
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky="new")

# Time Spinners (from_= and to= )
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)

# Placement on grid with label next to it
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=":").grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=":").grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)

# Adding padding to a widget
timeFrame['padx'] = 36

# Frame for the date spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

# Date Labels
dayLabel = tkinter.Label(dateFrame, text="Day")
monthLabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")

# Adding the Date Labels to the grid
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

# Date Spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)

# Adding the Date Spinners to the grid
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# Buttons
okButton = tkinter.Button(mainWindow, text="OK")
cancelButton = tkinter.Button(mainWindow, text="CANCEL", command=mainWindow.destroy)  # You can either use destroy

# Adding the Buttons to the grid
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')




mainWindow.mainloop()

print(rbValue.get())
