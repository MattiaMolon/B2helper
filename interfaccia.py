from tkinter import *
import requests
import json

def translate():
    parola = toTranslate.get()

    payload = {'from' : 'eng', 
           'dest' : 'eng', 
           'format' : 'json', 
           'phrase' : parola, 
           'pretty': 'true'}

    response = requests.get('https://glosbe.com/gapi/translate', params=payload)
    filejson = response.json()

    toPrint = ""
    for i in range(0,5):
        try:
            element = filejson['tuc'][i]

            trovato = False
            meaning = 'meaning not found'
            for elem in element['meanings']:
                if elem['language'] == 'en' and not trovato:
                    meaning = elem['text']
                    trovato = True
            
            toPrint += element['phrase']['text'] + ':    ' + meaning + '\n'
        except:
            pass


    global myLabel
    myLabel['text']=toPrint
    return toPrint


# window principal
rootW = Tk()
rootW.title('translator')
rootW.geometry('700x500+400+200')

# variabile stringa
toTranslate = StringVar()

# widget pulsante
myButton = Button(rootW, text ="traduci", command = translate)
myButton.place(relx = 0.5, rely = 0.5, anchor=CENTER)

# widget textbox
myTextBox = Entry(rootW, textvariable = toTranslate).place(relx = 0.5, rely = 0.4, anchor=CENTER)

# widget label
myLabel = Label(rootW, text='cose appariranno qui')
myLabel.pack()

rootW.mainloop()