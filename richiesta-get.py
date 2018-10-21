import requests
import json

parola = input('inserisci una parola da tradurre : ')

payload = {'from' : 'it', 
           'dest' : 'eng', 
           'format' : 'json', 
           'phrase' : parola, 
           'pretty': 'true'}

response = requests.get('https://glosbe.com/gapi/translate', params=payload)
filejson = response.json()


for i in range(0,5):
    try:
        element = filejson['tuc'][i]

        trovato = False
        meaning = 'meaning not found'
        for elem in element['meanings']:
            if elem['language'] == 'en' and not trovato:
                meaning = elem['text']
                trovato = True
            
        print(element['phrase']['text'] + '\t\t->\t\t' + meaning)
    except:
        pass

