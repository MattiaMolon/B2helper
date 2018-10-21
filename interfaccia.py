from tkinter import *

def helloCallBack():
    parola = toTranslate.get()
    myLabel = Label(rootW, text = parola).pack()
    return


# window principal
rootW = Tk()
rootW.title('translator')
rootW.geometry('500x500')

# variabile stringa
toTranslate = StringVar()

# widget pulsante
myButton = Button(rootW, text ="traduci", command = helloCallBack)
myButton.place(relx = 0.5, rely = 0.5, anchor=CENTER)

# widget textbox
myTextBox = Entry(rootW, textvariable = toTranslate).pack()



rootW.mainloop()