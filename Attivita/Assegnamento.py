import datetime
import os
import pickle


class Assegnamento:

    def __init__(self):
        self.codice = -1
        self.dataOraInizio = datetime.datetime(1970, 1, 1, 0, 0)
        self.dataOraFine = datetime.datetime(1970, 1, 1, 0, 0)
        self.servizio = None
        self.cliente = None

    def aggiungiAssegnamento(self, codice, dataOraInizio, dataOraFine, servizio, cliente):
        self.codice = codice
        self.dataOraInizio = dataOraInizio
        self.dataOraFine = dataOraFine
        self.servizio = servizio
        self.cliente = cliente
        assegnamenti = {}
        if os.path.isfile('Dati/Assegnamenti.pickle'):
            with open('Dati/Assegnamenti.pickle', 'rb') as f:
                assegnamenti = pickle.load(f)
        assegnamenti[codice] = self
        with open('Dati/Assegnamenti.pickle', 'wb') as handle:
            pickle.dump(assegnamenti, handle, pickle.HIGHEST_PROTOCOL)

    def getInfoAssegnamento(self):
        return {"codice": self.codice, "dataOraInizio": self.dataOraInizio, "dataOraFine": self.dataOraFine,
                "servizio": self.servizio, "cliente": self.cliente}

    def rimuoviAssegnamento(self):
        if os.path.isfile('Dati/Assegnamenti.pickle'):
            with open('Dati/Assegnamenti.pickle', 'rb') as f:
                assegnamenti = pickle.load(f)
                del assegnamenti[self.codice]
                with open('Dati/Assegnamenti.pickle', 'wb') as handle:
                    pickle.dump(assegnamenti, handle, pickle.HIGHEST_PROTOCOL)
                self.codice = -1
                self.dataOraInizio = datetime.datetime(1970, 1, 1, 0, 0)
                self.dataOraFine = datetime.datetime(1970, 1, 1, 0, 0)
                self.servizio = None
                self.cliente = None
                del self

    def verificaFine(self):
        return datetime.datetime.now() > self.dataOraFine
