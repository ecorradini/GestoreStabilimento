import datetime
import os
import pickle


class Ricevuta:

    def __init__(self):
        self.ammontareLordo = 0.0
        self.data = datetime.datetime(1970, 1, 1, 0, 0)
        self.prezzoIngresso = 0.0
        self.assegnamento = None

    def aggiungiRicevuta(self, data, ammontareLordo, prezzoIngresso, assegnamento):
        self.ammontareLordo = ammontareLordo
        self.data = data
        self.prezzoIngresso = prezzoIngresso
        self.assegnamento = assegnamento
        ricevute = {}
        if os.path.isfile('Dati/Ricevute.pickle'):
            with open('Dati/Ricevute.pickle', 'rb') as f:
                ricevute = pickle.load(f)
        ricevute[assegnamento.codice] = self
        with open('Dati/Ricevute.pickle', 'wb') as f:
            pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)

    def getInfoRicevuta(self):
        return {
            "ammontareLordo": self.ammontareLordo,
            "data": self.data,
            "prezzoIngresso": self.prezzoIngresso,
            "assegnamento": self.assegnamento
        }

    def rimuoviRicevuta(self):
        if os.path.isfile('Dati/Ricevute.pickle'):
            with open('Dati/Ricevute.pickle', 'wb+') as f:
                ricevute = dict(pickle.load(f))
                del ricevute[self.assegnamento.codice]
                pickle.dump(ricevute, f, pickle.HIGHEST_PROTOCOL)
        self.ammontareLordo = 0.0
        self.data = datetime.datetime(1970, 1, 1, 0, 0)
        self.prezzoIngresso = 0.0
        self.assegnamento = None
        del self