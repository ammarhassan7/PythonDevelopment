# Simple Python GUI Calculator using Tkinter

from tkinter import *

# Global variable to store the expression
expression = ""

# Function to update the expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the expression
def evaluate():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

# Function to clear the entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Driver code
if __name__ == "__main__":
    # Create the GUI window
    app = Tk()
    app.title("Basic Calculator")
    app.configure(background="light blue")
    app.geometry("270x200")

    # Variable to hold the current expression
    equation = StringVar()

    # Create the entry box for the expression
    expression_field = Entry(app, textvariable=equation, font=('Arial', 18))
    expression_field.grid(columnspan=4, ipadx=8, ipady=8)

    # Button configurations
    button_config = {'fg': 'black', 'bg': 'white', 'height': 2, 'width': 7}

    # Creating buttons
    Button(app, text='1', **button_config, command=lambda: press(1)).grid(row=2, column=0)
    Button(app, text='2', **button_config, command=lambda: press(2)).grid(row=2, column=1)
    Button(app, text='3', **button_config, command=lambda: press(3)).grid(row=2, column=2)
    Button(app, text='4', **button_config, command=lambda: press(4)).grid(row=3, column=0)
    Button(app, text='5', **button_config, command=lambda: press(5)).grid(row=3, column=1)
    Button(app, text='6', **button_config, command=lambda: press(6)).grid(row=3, column=2)
    Button(app, text='7', **button_config, command=lambda: press(7)).grid(row=4, column=0)
    Button(app, text='8', **button_config, command=lambda: press(8)).grid(row=4, column=1)
    Button(app, text='9', **button_config, command=lambda: press(9)).grid(row=4, column=2)
    Button(app, text='0', **button_config, command=lambda: press(0)).grid(row=5, column=0)
    Button(app, text='+', **button_config, command=lambda: press('+')).grid(row=2, column=3)
    Button(app, text='-', **button_config, command=lambda: press('-')).grid(row=3, column=3)
    Button(app, text='*', **button_config, command=lambda: press('*')).grid(row=4, column=3)
    Button(app, text='/', **button_config, command=lambda: press('/')).grid(row=5, column=3)
    Button(app, text='=', **button_config, command=evaluate).grid(row=5, column=2)
    Button(app, text='Clear', **button_config, command=clear).grid(row=5, column=1)
    Button(app, text='.', **button_config, command=lambda: press('.')).grid(row=6, column=0)

    # Start the GUI event loop
    app.mainloop()
