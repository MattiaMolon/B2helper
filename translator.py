import requests

class translator:

    def __init__(self, sourceLanguage = 'eng', targetLanguage = 'eng'):
        self.sourceL = sourceLanguage
        self.targetL = targetLanguage
        self.url = 'https://glosbe.com/gapi/translate'

        self.payload = {'from' : self.sourceL, 
                        'dest' : self.targetL, 
                        'format' : 'json', 
                        'phrase' : '', 
                        'pretty': 'true'}

    # actual function that translate a word and return a json 
    # with all it's definitions and translations 
    def translate (self, parola):
        self.payload['phrase'] = parola

        response = requests.get(self.url, self.payload)
        jsonFile = response.json()

        return jsonFile


        