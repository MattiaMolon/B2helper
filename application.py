import tkinter as tk

class Application:
    
    def __init__(self):
        # main window options
        self.mainW = tk.Tk()
        self.mainW.title("B2helper")

        # textBox variable
        self.toTranslate = tk.StringVar()
        
        # textBox init
        self.myTextBox = tk.Entry(self.mainW, textvariable = self.toTranslate)
        self.myTextBox.pack()

        # button init
        self.explaineButton = tk.Button(self.mainW, text ='explain to me', bg = 'white', fg = 'green')
        self.explaineButton.pack()

        # label init
        self.explainedText = tk.Label(self.mainW)
        self.explainedText.pack()

    
    def start(self):
        self.mainW.mainloop()

    def setButtonOption(self, function):
        self.explaineButton['command'] = function


        