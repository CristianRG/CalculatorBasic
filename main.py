from tkinter import *

class Calculator(Tk):

    def __init__(self):
        super().__init__()
        self.display = Entry(self, width=50, bg='gray')
        self.display.grid(row=0, column=0, columnspan=4, ipady=4, sticky=W+E)
        Calculator.geometry(self, '300x160')
        Calculator.title(self, 'Calculadora')

    def getNumbers(self, n):
        if(len(self.display.get()) == 0):
            self.display.insert(len(self.display.get()), '0')
            return
        elif('0' in self.display.get()[0]):
            self.display.delete(len(self.display.get())-1, END)

        self.display.insert(len(self.display.get()), n)
        return

    def getExpression(self, expression):
        if('0' in self.display.get()[0]):
            if(expression == '(' or '-'):
                self.display.delete(len(self.display.get())-1, END)
                self.display.insert(len(self.display.get()), expression)
            return
        else:
            self.display.insert(len(self.display.get()), expression)
        return

    def clearScreen(self):
        if('0' in self.display.get()[0]):
            return
        self.display.delete(0, END)
        Calculator.getNumbers(self, '0')   

    def undo(self):
        if('0' in self.display.get()[0]):
            return
        elif('Syntaxis ERROR' in self.display.get()):
            Calculator.clearScreen(self)
            return

        self.display.delete(len(self.display.get())-1, END)

        if(len(self.display.get()) == 0):
            Calculator.getNumbers(self, '0')
            return

    def getResult(self):

        result = self.display.get()

        try:
            self.display.delete(0, END)
            result = str(eval(result))

            if((type(result) == float) and (result/result) == 1.0):
                result = int(result)


            self.display.insert(0, result)
        except (SyntaxError, ZeroDivisionError):
            self.display.insert(0, 'Syntaxis ERROR')
        return


    def Buttons(self):

        # functiones
        Button(self, text='AC', command=lambda:Calculator.clearScreen(self)).grid(row=1, column=0, sticky=W+E)
        Button(self, text='<-', command=lambda:Calculator.undo(self)).grid(row=1,column=3, sticky=W+E)

        # expretiones
        Button(self, text='(', command=lambda:Calculator.getExpression(self, '(')).grid(row=1,column=1, sticky=W+E)
        Button(self, text=')', command=lambda:Calculator.getExpression(self, ')')).grid(row=1,column=2, sticky=W+E)

        Button(self, text='*', command=lambda:Calculator.getExpression(self, '*')).grid(row=2, column=3, sticky=W+E)
        Button(self, text='+', command=lambda:Calculator.getExpression(self, '+')).grid(row=3, column=3, sticky=W+E)
        Button(self, text='-', command=lambda:Calculator.getExpression(self, '-')).grid(row=4, column=3, sticky=W+E)
        Button(self, text='/', command=lambda:Calculator.getExpression(self, '/')).grid(row=5, column=2, sticky=W+E)
        Button(self, text='EXP', command=lambda:Calculator.getExpression(self, '**')).grid(row=5, column=0, sticky=W+E)

        Button(self, text='=', command=lambda:Calculator.getResult(self)).grid(row=5, column=3, sticky=W+E)

        # numers
        Button(self, text='9', command=lambda:Calculator.getNumbers(self, '9')).grid(row=2,column=0, sticky=W+E)
        Button(self, text='8', command=lambda:Calculator.getNumbers(self, '8')).grid(row=2,column=1, sticky=W+E)
        Button(self, text='7', command=lambda:Calculator.getNumbers(self, '7')).grid(row=2,column=2, sticky=W+E)

        Button(self, text='6', command=lambda:Calculator.getNumbers(self, '6')).grid(row=3,column=0, sticky=W+E)
        Button(self, text='5', command=lambda:Calculator.getNumbers(self, '5')).grid(row=3,column=1, sticky=W+E)
        Button(self, text='4', command=lambda:Calculator.getNumbers(self, '4')).grid(row=3,column=2, sticky=W+E)

        Button(self, text='3', command=lambda:Calculator.getNumbers(self, '3')).grid(row=4,column=0, sticky=W+E)
        Button(self, text='2', command=lambda:Calculator.getNumbers(self, '2')).grid(row=4,column=1, sticky=W+E)
        Button(self, text='1', command=lambda:Calculator.getNumbers(self, '1')).grid(row=4,column=2, sticky=W+E)

        Button(self, text='0', command=lambda:Calculator.getNumbers(self, '0')).grid(row=5,column=1, sticky=W+E)



    
calculator = Calculator()
calculator.getNumbers('0')
calculator.Buttons()
calculator.mainloop()
