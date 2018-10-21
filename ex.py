import application 
import translator as tr

def translate():
    parola = app.toTranslate.get()

    trans = tr.Translator()
    filejson = trans.translate(parola)
    

    toPrint = ""
    for i in range(0,5):
        try:
            element = filejson['tuc'][i]

            trovato = False
            meaning = 'meaning not found'
            for elem in element['meanings']:
                if elem['language'] == trans.targetL and not trovato:
                    meaning = elem['text']
                    trovato = True
            
            toPrint += element['phrase']['text'] + ':    ' + meaning + '\n'
        except:
            pass


    app.explainedText['text']=toPrint
    return toPrint


app = application.Application()
app.setButtonOption(translate)
app.start()
