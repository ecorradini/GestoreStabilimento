import datetime
import os.path
import pickle

class Abbonamento:

    def __init__(self):
        self.codice = -1
        self.dataInizio = datetime.datetime(1970, 1, 1, 0, 0)
        self.dataRilascio = datetime.datetime(1970, 1, 1, 0, 0)
        self.dataScadenza = datetime.datetime(1970, 1, 1, 0, 0)
        self.stagionale = False

    def aggiungiAbbonamento(self, codice, dataInizio, dataRilascio, dataScadenza, stagionale):
        self.codice = codice
        self.dataInizio = dataInizio
        self.dataRilascio = dataRilascio
        self.dataScadenza = dataScadenza
        self.stagionale = stagionale
        abbonamenti = {}
        if os.path.isfile('Dati/Abbonamenti.pickle'):
            with open('Dati/Abbonamenti.pickle', 'rb') as f:
                abbonamenti = pickle.load(f)
        abbonamenti[codice] = self
        with open('Dati/Abbonamenti.pickle', 'wb') as f:
            pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)

    def getInfoAbbonamento(self):
        return {
            "codice": self.codice,
            "dataInizio": self.dataInizio,
            "dataRilascio": self.dataRilascio,
            "dataScadenza": self.dataScadenza,
            "stagionale": self.stagionale
        }

    def ricercaAbbonamento(self, codice):
        if os.path.isfile('Dati/Abbonamenti.pickle'):
            with open('Dati/Abbonamenti.pickle', 'rb') as f:
                abbonamenti = pickle.load(f)
                return abbonamenti[codice]
        else:
            return None

    def rimuoviAbbonamento(self):
        if os.path.isfile('Dati/Abbonamenti.pickle'):
            with open('Dati/Abbonamenti.pickle', 'wb+') as f:
                abbonamenti = pickle.load(f)
                del abbonamenti[self.codice]
                pickle.dump(abbonamenti, f, pickle.HIGHEST_PROTOCOL)
        self.codice = -1
        self.dataInizio = datetime.datetime(1970, 1, 1, 0, 0)
        self.dataRilascio = datetime.datetime(1970, 1, 1, 0, 0)
        self.dataScadenza = datetime.datetime(1970, 1, 1, 0, 0)
        self.stagionale = False
        del self

    def verificaScaduto(self):
        return datetime.datetime.now() > self.dataScadenza
