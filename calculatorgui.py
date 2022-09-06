# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.


# firmware development engineering


# Needs to fix the bug where the user is able to enter a number after the result is given which ultimately changes the number.
try:
    import tkinter
    import tkinter.font as font
except ImportError:
    import Tkinter as tkinter

calculator_numbers = ['AC', 'Del', '%', '/', '7', '8', '9', '*',
                      '4', '5', '6', '-',
                      '1', '2', '3', '+',
                      '0', '.', '='
                      ]

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('400x400+8+400')
mainWindow.minsize(300, 200)
mainWindow.maxsize(600, 500)

mainWindow["padx"] = 50
mainWindow["bg"] = "#000000"


def button_text(text: str) -> bool:
    """
    Describes the button functionality of the calculator
    :param text: The text of the button being pressed
    """
    # result.delete(0, "end")
    number = str(result.get())
    string_list = number.split()
    if text == '=':
        if len(string_list) == 1 or len(string_list) == 0 or len(string_list) == 2:
            pass
        elif len(string_list) > 3:
            pass
        else:
            if string_list[1] == '+':
                if '.' in string_list[0]:
                    final = float(string_list[0]) + int(string_list[2])
                    result.configure(state=tkinter.NORMAL)
                    result.delete(0, "end")
                    result.insert("end", str(final))
                    result.configure(state=tkinter.DISABLED)
                    return True

                elif '.' in string_list[2]:
                    final = int(string_list[0]) + float(string_list[2])
                    result.configure(state=tkinter.NORMAL)
                    result.delete(0, "end")
                    result.insert("end", str(final))
                    result.configure(state=tkinter.DISABLED)
                    return True
                else:
                    final = int(string_list[0]) + int(string_list[2])
                    result.configure(state=tkinter.NORMAL)
                    result.delete(0, "end")
                    result.insert("end", str(final))
                    result.configure(state=tkinter.DISABLED)
                    print(len(string_list))
                    return True

            if string_list[1] == '-':
                if '.' in string_list[0]:
                    final = float(string_list[0]) - int(string_list[2])
                    result.configure(state=tkinter.NORMAL)
                    result.delete(0, "end")
                    result.insert("end", str(final))
                    result.configure(state=tkinter.DISABLED)
                    return True
                elif '.' in string_list[2]:
                    final = int(string_list[0]) - float(string_list[2])
                    result.configure(state=tkinter.NORMAL)
                    result.delete(0, "end")
                    result.insert("end", str(final))
                    result.configure(state=tkinter.DISABLED)
                    return True
                else:
                    final = int(string_list[0]) - int(string_list[2])
                    result.configure(state=tkinter.NORMAL)
                    result.delete(0, "end")
                    result.insert("end", str(final))
                    result.configure(state=tkinter.DISABLED)
                    return True

            if string_list[1] == '*':
                if '.' in string_list[0]:
                    final = float(string_list[0]) * int(string_list[2])
                    result.configure(state=tkinter.NORMAL)
                    result.delete(0, "end")
                    result.insert("end", str(final))
                    result.configure(state=tkinter.DISABLED)
                    return True
                elif '.' in string_list[2]:
                    final = int(string_list[0]) * float(string_list[2])
                    result.configure(state=tkinter.NORMAL)
                    result.delete(0, "end")
                    result.insert("end", str(final))
                    result.configure(state=tkinter.DISABLED)
                    return True
                else:
                    final = int(string_list[0]) * int(string_list[2])
                    result.configure(state=tkinter.NORMAL)
                    result.delete(0, "end")
                    result.insert("end", str(final))
                    result.configure(state=tkinter.DISABLED)
                    return True

            if string_list[1] == '/':
                if '.' in string_list[0]:
                    try:
                        final = float(string_list[0]) / int(string_list[2])
                    except ZeroDivisionError:
                        result.configure(state=tkinter.NORMAL)
                        result.delete(0, "end")
                        result.insert("end", "0")
                        result.configure(state=tkinter.DISABLED)
                        return True
                    else:
                        result.configure(state=tkinter.NORMAL)
                        result.delete(0, "end")
                        result.insert("end", str(final))
                        result.configure(state=tkinter.DISABLED)
                        return True
                elif '.' in string_list[2]:
                    try:
                        final = int(string_list[0]) / float(string_list[2])
                    except ZeroDivisionError:
                        result.configure(state=tkinter.NORMAL)
                        result.delete(0, "end")
                        result.insert("end", "0")
                        result.configure(state=tkinter.DISABLED)
                        return True
                    else:
                        result.configure(state=tkinter.NORMAL)
                        result.delete(0, "end")
                        result.insert("end", str(final))
                        result.configure(state=tkinter.DISABLED)
                        return True
                else:
                    try:
                        final = int(string_list[0]) / int(string_list[2])
                    except ZeroDivisionError:
                        result.configure(state=tkinter.NORMAL)
                        result.delete(0, "end")
                        result.insert("end", "0")
                        result.configure(state=tkinter.DISABLED)
                        return True
                    else:
                        result.configure(state=tkinter.NORMAL)
                        result.delete(0, "end")
                        result.insert("end", str(final))
                        result.configure(state=tkinter.DISABLED)
                        return True

    elif text == 'AC':
        result.configure(state=tkinter.NORMAL)
        result.delete(0, "end")
        result.configure(state=tkinter.DISABLED)
        del string_list
        return True
    elif text == "Del":
        result.configure(state=tkinter.NORMAL)
        if len(string_list) == 3:
            if len(string_list[2]) == 1:
                result.delete(len(string_list[0]) + 3, "end")
                result.configure(state=tkinter.DISABLED)
                string_list.remove(string_list[2])
                return True
            else:
                result.delete(len(string_list[0]) + 2 + len(string_list[2]), "end")
                result.configure(state=tkinter.DISABLED)
                return True
        if len(string_list) == 2:
            result.delete(len(string_list[0]) + 1, "end")
            result.configure(state=tkinter.DISABLED)
            string_list.remove(string_list[1])
            return True
        if len(string_list) == 1:
            if len(string_list[0]) == 1:
                result.delete(0, "end")
                result.configure(state=tkinter.DISABLED)
                del string_list
                return True
            else:
                result.delete(len(string_list[0]) - 1, "end")
                result.configure(state=tkinter.DISABLED)
                return True
    elif text == "%":
        if len(string_list) == 0 or len(string_list) == 2:
            pass
        elif len(string_list) == 1:
            if "." in string_list[0]:
                x = float(string_list[0])
                x = str(x / 100)
                result.configure(state=tkinter.NORMAL)
                result.delete(0, "end")
                result.insert("end", x)
                result.configure(state=tkinter.DISABLED)
                return True
            else:
                x = int(string_list[0])
                x = str(x / 100)
                result.configure(state=tkinter.NORMAL)
                result.delete(0, "end")
                result.insert("end", x)
                result.configure(state=tkinter.DISABLED)
                return True
        elif len(string_list) == 3:
            if "." in string_list[2]:
                x = float(string_list[2])
                x = str(x / 100)
                result.configure(state=tkinter.NORMAL)
                result.delete(len(string_list[0]) + 3, "end")
                result.insert("end", x)
                result.configure(state=tkinter.DISABLED)
                return True
            else:
                x = int(string_list[2])
                x = str(x / 100)
                result.configure(state=tkinter.NORMAL)
                result.delete(len(string_list[0]) + 3, "end")
                result.insert("end", x)
                result.configure(state=tkinter.DISABLED)
                return True

    elif (text == "+") or (text == "*") or (text == "/") or (text == "-"):
        if len(string_list) == 0:
            pass
        elif len(string_list) == 1:
            result.configure(state=tkinter.NORMAL)
            result.insert("end", " " + text + " ")
            result.configure(state=tkinter.DISABLED)
            return True
        elif number[len(string_list) - 2] == "+" or (number[len(string_list) - 2] == "-") \
                or (number[len(string_list) - 2] == "*") or (number[len(string_list) - 2] == "/"):
            pass
        elif len(string_list) >= 3:
            pass
        else:
            result.configure(state=tkinter.NORMAL)
            result.insert("end", " " + text + " ")
            result.configure(state=tkinter.DISABLED)
            return True
    else:
        return False


def button_track(text: str) -> None:
    number = str(result.get())
    string_list = number.split()
    print(text)
    if text == '1':
            if len(string_list) > 3:
                pass
            elif len(string_list) == 3:
                result.configure(state=tkinter.NORMAL)
                result.delete(0, "end")
                del string_list
                result.insert("end", text)
                result.configure(state=tkinter.DISABLED)
            else:
                result.configure(state=tkinter.NORMAL)
                result.insert("end", text)
                result.configure(state=tkinter.DISABLED)
                print(len(string_list))


    elif text == '2':
        if len(string_list) > 3:
            pass
        elif len(string_list) == 3:
            result.configure(state=tkinter.NORMAL)
            result.delete(0, "end")
            del string_list
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
        else:
            result.configure(state=tkinter.NORMAL)
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
            print(len(string_list))
    elif text == '3':
        if len(string_list) > 3:
            pass
        elif len(string_list) == 3:
            result.configure(state=tkinter.NORMAL)
            result.delete(0, "end")
            del string_list
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
        else:
            result.configure(state=tkinter.NORMAL)
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
            print(len(string_list))
    elif text == '4':
        if len(string_list) > 3:
            pass
        elif len(string_list) == 3:
            result.configure(state=tkinter.NORMAL)
            result.delete(0, "end")
            del string_list
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
        else:
            result.configure(state=tkinter.NORMAL)
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
            print(len(string_list))
    elif text == '5':
        if len(string_list) > 3:
            pass
        elif len(string_list) == 3:
            result.configure(state=tkinter.NORMAL)
            result.delete(0, "end")
            del string_list
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
        else:
            result.configure(state=tkinter.NORMAL)
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
            print(len(string_list))
    elif text == '6':
        if len(string_list) > 3:
            pass
        elif len(string_list) == 3:
            result.configure(state=tkinter.NORMAL)
            result.delete(0, "end")
            del string_list
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
        else:
            result.configure(state=tkinter.NORMAL)
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
            print(len(string_list))
    elif text == '7':
        if len(string_list) > 3:
            pass
        elif len(string_list) == 3:
            result.configure(state=tkinter.NORMAL)
            result.delete(0, "end")
            del string_list
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
        else:
            result.configure(state=tkinter.NORMAL)
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
            print(len(string_list))
    elif text == '8':
        if len(string_list) > 3:
            pass
        elif len(string_list) == 3:
            result.configure(state=tkinter.NORMAL)
            result.delete(0, "end")
            del string_list
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
        else:
            result.configure(state=tkinter.NORMAL)
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
            print(len(string_list))
    elif text == '9':
        if len(string_list) > 3:
            pass
        elif len(string_list) == 3:
            result.configure(state=tkinter.NORMAL)
            result.delete(0, "end")
            del string_list
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
        else:
            result.configure(state=tkinter.NORMAL)
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
            print(len(string_list))
    elif text == '0':
        if len(string_list) > 3:
            pass
        elif len(string_list) == 3:
            result.configure(state=tkinter.NORMAL)
            result.delete(0, "end")
            del string_list
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
        else:
            result.configure(state=tkinter.NORMAL)
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
            print(len(string_list))
    else:
        if len(string_list) > 3:
            pass
        elif len(string_list) == 3:
            result.configure(state=tkinter.NORMAL)
            result.delete(0, "end")
            del string_list
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
        else:
            result.configure(state=tkinter.NORMAL)
            result.insert("end", text)
            result.configure(state=tkinter.DISABLED)
            print(len(string_list))


# Creating the result field
result = tkinter.Entry(mainWindow, relief="sunken", state="disabled")
result.grid(row=0, column=0, columnspan=4, sticky='ew')
result['font'] = font.Font(size=30)
# Creating the buttons for the GUI


newButton1 = tkinter.Button(mainWindow, text=calculator_numbers[0],
                            command=lambda: button_text(newButton1.cget('text')), bg='red', fg="#000000", borderwidth=5)
newButton1.grid(row=1, column=0, sticky='news')
newButton2 = tkinter.Button(mainWindow, text=calculator_numbers[1],
                            command=lambda: button_text(newButton2.cget('text')), bg='#D9D9D9', fg="#000000")
newButton2.grid(row=1, column=1, sticky='news')
newButton3 = tkinter.Button(mainWindow, text=calculator_numbers[2],
                            command=lambda: button_text(newButton3.cget('text')), bg='#D9D9D9', fg="#000000")
newButton3.grid(row=1, column=2, sticky='news')
newButton4 = tkinter.Button(mainWindow, text=calculator_numbers[3],
                            command=lambda: button_text(newButton4.cget('text')), bg="#ffa500", fg="#ffffff")
newButton4.grid(row=1, column=3, sticky='news')
newButton5 = tkinter.Button(mainWindow, text=calculator_numbers[4],
                            command=lambda: button_track(newButton5.cget('text')),
                            bg="#3B3B3B", fg="#ffffff")
newButton5.grid(row=2, column=0, sticky='news')
newButton6 = tkinter.Button(mainWindow, text=calculator_numbers[5],
                            command=lambda: button_track(newButton6.cget('text')), bg="#3B3B3B", fg="#ffffff")
newButton6.grid(row=2, column=1, sticky='news')
newButton7 = tkinter.Button(mainWindow, text=calculator_numbers[6],
                            command=lambda: button_track(newButton7.cget('text')), bg="#3B3B3B", fg="#ffffff")
newButton7.grid(row=2, column=2, sticky='news')
newButton8 = tkinter.Button(mainWindow, text=calculator_numbers[7],
                            command=lambda: button_text(newButton8.cget('text')), bg="#ffa500", fg="#ffffff")
newButton8.grid(row=2, column=3, sticky='news')
newButton9 = tkinter.Button(mainWindow, text=calculator_numbers[8],
                            command=lambda: button_track(newButton9.cget('text')), bg="#3B3B3B", fg="#ffffff")
newButton9.grid(row=3, column=0, sticky='news')
newButton10 = tkinter.Button(mainWindow, text=calculator_numbers[9],
                             command=lambda: button_track(newButton10.cget('text')), bg="#3B3B3B", fg="#ffffff")
newButton10.grid(row=3, column=1, sticky='news')
newButton11 = tkinter.Button(mainWindow, text=calculator_numbers[10],
                             command=lambda: button_track(newButton11.cget('text')), bg="#3B3B3B", fg="#ffffff")
newButton11.grid(row=3, column=2, sticky='news')
newButton12 = tkinter.Button(mainWindow, text=calculator_numbers[11],
                             command=lambda: button_text(newButton12.cget('text')), bg="#ffa500", fg="#ffffff")
newButton12.grid(row=3, column=3, sticky='news')
newButton13 = tkinter.Button(mainWindow, text=calculator_numbers[12],
                             command=lambda: button_track(newButton13.cget('text')), bg="#3B3B3B", fg="#ffffff")
newButton13.grid(row=4, column=0, sticky='news')
newButton14 = tkinter.Button(mainWindow, text=calculator_numbers[13],
                             command=lambda: button_track(newButton14.cget('text')), bg="#3B3B3B", fg="#ffffff")
newButton14.grid(row=4, column=1, sticky='news')
newButton15 = tkinter.Button(mainWindow, text=calculator_numbers[14],
                             command=lambda: button_track(newButton15.cget('text')), bg="#3B3B3B", fg="#ffffff")
newButton15.grid(row=4, column=2, sticky='news')
newButton16 = tkinter.Button(mainWindow, text=calculator_numbers[15],
                             command=lambda: button_text(newButton16.cget('text')), bg="#ffa500", fg="#ffffff")
newButton16.grid(row=4, column=3, sticky='news')
newButton17 = tkinter.Button(mainWindow, text=calculator_numbers[16],
                             command=lambda: button_track(newButton17.cget('text')), bg="#3B3B3B", fg="#ffffff")
newButton17.grid(row=5, column=0, columnspan=2, sticky='news')
newButton18 = tkinter.Button(mainWindow, text=calculator_numbers[17],
                             command=lambda: button_track(newButton18.cget('text')), bg="#3B3B3B", fg="#ffffff")
newButton18.grid(row=5, column=2, sticky='news')
newButton19 = tkinter.Button(mainWindow, text=calculator_numbers[18],
                             command=lambda: button_text(newButton19.cget('text')), bg="#ffa500", fg="#ffffff")
newButton19.grid(row=5, column=3, sticky='news')

# Styling the calculator

# Styling the columns
mainWindow.columnconfigure(0, weight=1000)
mainWindow.columnconfigure(1, weight=1000)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=1000)
mainWindow.columnconfigure(4, weight=1000)

# Styling the rows
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)

mainWindow.mainloop()
