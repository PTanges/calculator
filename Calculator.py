import tkinter
import math

'''
Simple Calculator using tkinter module for GUI
Calculator may only accept one operation at a time before clearing and does not accept compounding operations
- The calculator will accept one operation after x! sqrt x^ x^3 and then will clear
'''

class Calculator:
    def __init__(self):
        # Create Constructor with 8 rows
        self._mainWindow = tkinter.Tk()
        self._mainWindow.title("Calculator")
        self._numberLimit = 14
        self._display = ""
        self._plusMinus = ""
        self._errorString = ""
        self._input = 0.0
        self._priorCommand = ""

        self._f1 = tkinter.Frame(self._mainWindow)
        self._f2 = tkinter.Frame(self._mainWindow)
        self._f3 = tkinter.Frame(self._mainWindow)
        self._f4 = tkinter.Frame(self._mainWindow)
        self._f5 = tkinter.Frame(self._mainWindow)
        self._f6 = tkinter.Frame(self._mainWindow)
        self._f7 = tkinter.Frame(self._mainWindow)
        self._f8 = tkinter.Frame(self._mainWindow)

        self._numSign = tkinter.StringVar()
        self._labelSign = tkinter.Label(self._f1, textvariable=self._numSign, relief="sunken")
        self._numberDisplay = tkinter.StringVar()
        self._labelDisplay = tkinter.Label(self._f1, textvariable=self._numberDisplay, relief="sunken")
        self._labelFormat = tkinter.Label(self._f2)
        self._errorMessage = tkinter.StringVar()
        self._labelErrorLine = tkinter.Label(self._f2, textvariable=self._errorMessage, relief="sunken")

        self._labelSign.config(height=3, width=5)
        self._labelDisplay.config(height=3, width=35)
        self._labelFormat.config(height=1, width=10)
        self._labelErrorLine.config(height=1, width=20)

        self._buttonFactorial = tkinter.Button(self._f3, text="x!", command=self.factorialCallback)
        self._buttonSquareRoot = tkinter.Button(self._f3, text="√x", command=self.squareRootCallback)
        self._buttonPercentage = tkinter.Button(self._f3, text="%", command=self.percentageCallback)
        self._buttonNumSquared = tkinter.Button(self._f3, text="^2", command= lambda: self.exponentCallback(2))
        self._buttonNumCubed = tkinter.Button(self._f3, text="^3", command= lambda: self.exponentCallback(3))
        self._buttonPlusMinus = tkinter.Button(self._f4, text="+/-", command=self.plusMinusCallback)

        self._buttonNumber7 = tkinter.Button(self._f4, text="7", command= lambda: self.appendNumberCallback('7'))
        self._buttonNumber8 = tkinter.Button(self._f4, text="8", command= lambda: self.appendNumberCallback('8'))
        self._buttonNumber9 = tkinter.Button(self._f4, text="9", command= lambda: self.appendNumberCallback('9'))
        self._buttonNumber4 = tkinter.Button(self._f5, text="4", command= lambda: self.appendNumberCallback('4'))
        self._buttonNumber5 = tkinter.Button(self._f5, text="5", command= lambda: self.appendNumberCallback('5'))
        self._buttonNumber6 = tkinter.Button(self._f5, text="6", command= lambda: self.appendNumberCallback('6'))
        self._buttonNumber1 = tkinter.Button(self._f6, text="1", command= lambda: self.appendNumberCallback('1'))
        self._buttonNumber2 = tkinter.Button(self._f6, text="2", command= lambda: self.appendNumberCallback('2'))
        self._buttonNumber3 = tkinter.Button(self._f6, text="3", command= lambda: self.appendNumberCallback('3'))
        self._buttonNumber0 = tkinter.Button(self._f7, text="0", command= lambda: self.appendNumberCallback('0'))

        self._buttonAdd = tkinter.Button(self._f4, text="+", command= lambda: self.calculateEquationCallback('+'))
        self._buttonSubtract = tkinter.Button(self._f5, text="-", command= lambda: self.calculateEquationCallback('-'))
        self._buttonMultiply = tkinter.Button(self._f6, text="x", command= lambda: self.calculateEquationCallback('x'))
        self._buttonDivide = tkinter.Button(self._f7, text="/", command= lambda: self.calculateEquationCallback('/'))

        self._buttonDecimal = tkinter.Button(self._f7, text=".", command=self.decimalCallback)
        self._buttonCalculate = tkinter.Button(self._f7, text="=", command= lambda: self.calculateEquationCallback('='))

        self._buttonClear = tkinter.Button(self._f5, text="C", command=self.clearCallback)
        self._buttonAllClear = tkinter.Button(self._f6, text="AC", command=self.allClearCallback)
        self._buttonHistory = tkinter.Button(self._f7, text="H", command=self.historyCallback)
        self._buttonExit = tkinter.Button(self._f8, text="Exit", command=self._mainWindow.destroy)

        self._labelSign.pack(padx=5, side="left")
        self._labelDisplay.pack(padx=5, side="left")
        self._labelErrorLine.pack(padx=10, side="right")
        self._labelFormat.pack(padx=10, side="right")

        self._buttonFactorial.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonSquareRoot.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonPercentage.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonNumSquared.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonNumCubed.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)

        self._buttonPlusMinus.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonClear.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonAllClear.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonHistory.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonExit.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)

        self._buttonNumber7.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonNumber8.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonNumber9.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonNumber4.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonNumber5.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonNumber6.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonNumber1.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonNumber2.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonNumber3.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonNumber0.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)

        self._buttonDecimal.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonCalculate.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)

        self._buttonAdd.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonSubtract.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonMultiply.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)
        self._buttonDivide.pack(padx=10, pady=5, side="left", ipadx=5, ipady=2)

        self._f1.pack(padx=40, pady=15)
        self._f2.pack(padx=40, pady=15)
        self._f3.pack(padx=40)
        self._f4.pack(padx=40)
        self._f5.pack(padx=40)
        self._f6.pack(padx=40)
        self._f7.pack(padx=40)
        self._f8.pack(padx=40, pady=30)

        self._history = {}
        self.recordHistory()
        self.updateDisplay()

        tkinter.mainloop()

    def factorialCallback(self):
        # Run with proper _display input, soft input limit of 99 due to infinity
        if not "." in self._display and self._display != "":
            if int(self._display) >= 3 and int(self._display) < 100 and self._plusMinus != "-":
                # Basic Formula: factorial = n * (n-1)!
                i = 1.0
                self._display = int(self._display)
                while self._display > 1.0:
                    i *= self._display
                    self._display -= 1
                self._display = str(i)

                # Output formatting when number becomes e+, infinity, or trailing decimal of .0
                if "e" in self._display:
                    r = ""
                    for i in range(len(self._display)):
                        if self._display[i] == "e":
                            r += self._display[i:len(self._display)]
                            self._display = self._display[0:self._numberLimit - len(r)] + r
                            break
                    self._errorString = "Error: Number Overflow"
                elif self._display == "inf":
                    self._display = ""
                    self._errorString = "Error: infinity"
                elif len(self._display) > self._numberLimit:
                    self._display = self._display[0:self._numberLimit]
                elif self._display.endswith(".0"):
                    self._display = self._display[0:len(self._display) - 2]
            else:
                self._errorString = "Error: x! range [3:99]"

        self.updateDisplay()

    def squareRootCallback(self):
        '''
        Invariant: num must be > 0 (not negative)
        '''
        if self._plusMinus == "-":
            self._errorString = "Error: Negative in √x"
        elif len(self._display) > 0:
            if "." not in self._display:
                self._display = str(math.sqrt(int(self._display)))
            else:
                self._display = str(math.sqrt(float(self._display)))
            if len(self._display) > self._numberLimit:
                self._display = self._display[0:self._numberLimit]
            elif self._display.endswith(".0"):
                self._display = self._display[0:len(self._display)-2]
        self.updateDisplay()

    def percentageCallback(self):
        '''
        Invariant: % out of 100
        '''
        if len(self._display) > 0 and self._plusMinus != "-" and float(self._display) >= 1 and float(self._display) <= 100:
            self._display = str(float(self._display) / 100.0)
        elif len(self._display) > 0 and float(self._display) > 0.01 and float(self._display) < 1.0 and self._plusMinus != "-":
            self._display = str(float(self._display) * 100.0)
            if self._display.endswith(".0"):
                self._display = self._display[0:len(self._display)-2]
        else:
            self._errorString = "Error: % range [1:100]"
        self._input = float(self._display)
        self.updateDisplay()

    def exponentCallback(self, exponent):
        # x Square or x Cube, may be easily modified to accept user input of integer. May require additional ifs for x^0
        if len(self._display) > 0 and len(self._display) <= (self._numberLimit):
            if exponent % 2 == 0:
                self._plusMinus = "+"
            t = float(self._display)
            for i in range(exponent-1):
                t *= float(self._display)
            self._display = str(t)

            # Output formatting when number becomes e+, infinity, or trailing decimal of .0
            if "e" in self._display:
                r = ""
                for i in range(len(self._display)):
                    if self._display[i] == "e":
                        r += self._display[i:len(self._display)]
                        self._display = self._display[0:self._numberLimit - len(r)] + r
                        break
                self._errorString = "Error: Number Overflow"
            elif self._display == "inf":
                self._display = ""
                self._errorString = "Error: infinity"
            elif len(self._display) > self._numberLimit:
                self._display = self._display[0:self._numberLimit]
            elif self._display.endswith(".0"):
                self._display = self._display[0:len(self._display) - 2]
            self._input = float(self._display)
        self.updateDisplay()

    # Prevent leading 0 in self._display while also having default 0 in self._numberDisplay label StringVar
    def appendNumberCallback(self, appendNum):
        if len(self._display) < 1 and appendNum == "0":
            pass
        elif len(self._display) == 1 and int(self._display) == 0 and appendNum != "0":
            self._display = appendNum
        else:
            self._display += appendNum
        self.updateDisplay()

    def clearCallback(self):
        # Backspace equivalent
        if len(self._display) > 0:
            self._display = self._display[0:-1]
        if len(self._display) < 1:
            self._plusMinus = ""
        if len(self._display) == 1:
            if self._display[0] == "0":
                self._display = ""
        self.updateDisplay()

    def allClearCallback(self):
        # Reset all variables
        self._display = ""
        self._plusMinus = ""
        self._input = 0.0
        self._priorCommand = ""
        self.updateDisplay()

    # Easter Egg Password breaker
    def historyCallback(self):
        self.updateDisplay()
        if len(self._display) > 0:
            try:
                self._numberDisplay.set(self._history[self._display])
                self._errorMessage.set("Key: " + self._display)
            except KeyError:
                self._errorMessage.set("Error: KeyError")
        else:
            self._errorMessage.set("Error: No Password Given")

    def plusMinusCallback(self):
        # +/- Sign
        if self._plusMinus == "-":
            self._plusMinus = "+"
        else:
            self._plusMinus = "-"
        self.updateDisplay()

    def calculateEquationCallback(self, newCommand):
        # Initial input declaration/fill data
        if len(self._display) > 0 and newCommand != "=" and self._priorCommand == "":
            self._input = float(self._display)
            self._display = ""
        elif self._display != "" and self._input == 0.0:
            self._input = float(self._display)
            self._display = ""

        if newCommand != "=":
            self._priorCommand = newCommand

        if self._input == 0.0:
            self.allClearCallback()

        if newCommand == "=" and self._priorCommand != newCommand and self._display != "":
            p = float(self._display)
            if self._plusMinus == "-":
                p *= -1

            # The Four Basic Arithmetic
            if self._priorCommand == "+":
                self._display = str(self._input + p)
            elif self._priorCommand == "-":
                self._display = str(self._input - p)
            elif self._priorCommand == "x":
                self._display = str(self._input * p)
            elif self._priorCommand == "/":
                if p != 0.0:
                    self._display = str(self._input / p)

            if float(self._display) < 0:
                self._numSign.set("-")

            if self._display!= "":
                if self._display.endswith(".0"):
                    self._display = self._display[0:len(self._display) - 2]
                self._input = float(self._display)
            if self._priorCommand == "=":
                self._priorCommand = ""
                self._input = 0.0

            # Clear All Data
            self._numberDisplay.set(self._display)
            self._display = ""
            self._input = 0.0
            self._priorCommand = ""
            self._plusMinus = ""

    def decimalCallback(self):
        # Add . decimal to _display buffer
        if '.' not in self._display:
            if len(self._display) < 1:
                self._display = "0."
            else:
                self._display += '.'
        self.updateDisplay()

    def updateDisplay(self):
        print("Display:\t", self._display)
        print("Input:\t", self._input)
        print("\n========\n")

        # Update or clear Sign Display and Error
        if len(self._display) > self._numberLimit:
            self._numberDisplay.set(self._display[0:self._numberLimit])
            self._errorMessage.set("Error: Value Overflow")
            self._display = ""
        elif len(self._display) < 1:
            self._numberDisplay.set("0")
            self._errorMessage.set("")
        else:
            self._numberDisplay.set(self._display)
            self._errorMessage.set(self._errorString)
            if self._errorString != "":
                self._display = ""
                self._plusMinus = ""
        self._numSign.set(self._plusMinus)
        self._errorString = ""


    def recordHistory(self):
        # Easter Egg
        self._history["1984"] = "Oink Oink"
        self._history["0.1134"] = "Hey John"
        self._history["123123"] = "321321"
        self._history["16120201514"] = "That's me!"
        self._history["16120189311"] = "That's my nickname!"
        self._history["2845"] = "Stanley randomly guessed\nall the correct numbers"
        self._history["3.14"] = "I prefer cake to be quite honest"
        self._history["99999999999999"] = "That's like... infinity!"
        self._history["0.112358132134"] = "Smart cookie"
        self._history["2012"] = "The world is ending... it was nice knowing you"
        self._history["2048"] = "Remember flappy bird, kid?"
        self._history["911"] = "Back in my day..."
        self._history["2020"] = "https://www.youtube.com/\nwatch?v=dQw4w9WgXcQ"
        self._history["0.8261982"] = "Because it's the one thing\nyou can't replace"
        self._history["0.8211990"] = "If you want love,\nlower your expecations"