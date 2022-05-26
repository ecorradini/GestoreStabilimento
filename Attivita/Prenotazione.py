import datetime
import os
import pickle


class Prenotazione:

    def __init__(self):
        self.codice = -1
        self.dataOraInizio = datetime.datetime(1970, 1, 1, 0, 0)
        self.dataOraFine = datetime.datetime(1970, 1, 1, 0, 0)
        self.servizio = None
        self.cliente = None

    def aggiungiPrenotazione(self, codice, dataOraInizio, dataOraFine, servizio, cliente):
        self.codice = codice
        self.dataOraFine = dataOraFine
        self.dataOraInizio = dataOraInizio
        self.servizio = servizio
        self.cliente = cliente
        prenotazioni = {}
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
        prenotazioni[codice] = self
        with open('Dati/Prenotazioni.pickle', 'wb') as handle:
            pickle.dump(prenotazioni, handle, pickle.HIGHEST_PROTOCOL)

    def getInfoPrenotazione(self):
        return {"codice": self.codice, "dataOraInizio": self.dataOraInizio, "dataOraFine": self.dataOraFine,
                "servizio": self.servizio, "cliente": self.cliente}

    def disdiciPrenotazione(self):
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
                del prenotazioni[self.codice]
                with open('Dati/Prenotazioni.pickle', 'wb') as handle:
                    pickle.dump(prenotazioni, handle, pickle.HIGHEST_PROTOCOL)
                self.codice = -1
                self.dataOraInizio = datetime.datetime(1970, 1, 1, 0, 0)
                self.dataOraFine = datetime.datetime(1970, 1, 1, 0, 0)
                self.servizio = None
                self.cliente = None
                del self

    def verificaFine(self):
        if datetime.datetime.now() > self.dataOraFine:
            return True
        else:
            return False




