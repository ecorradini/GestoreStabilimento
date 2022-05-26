import os.path
import pickle

from Attivita.Utilizzatore import Utilizzatore

class Cliente(Utilizzatore):

    def __init__(self):
        super().__init__()
        self.abbonamenti = []
        self.note = ""

    def aggiungiCliente(self, note, abbonamenti, nome, telefono, email, cognome, dataNascita, codiceFiscale, codice):
        self.aggiungiUtilizzatore(telefono, nome, email, dataNascita, cognome, codiceFiscale, codice)
        self.note = note
        self.abbonamenti = abbonamenti
        clienti = {}
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        clienti[codice] = self
        with open('Dati/Clienti.pickle', 'wb') as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)


    def getInfoCliente(self):
        info = self.getInfoUtilizzatore()
        info["abbonamenti"] = self.abbonamenti
        info["note"] = self.note
        return info

    def ricercaUtilizzatoreNomeCognome(self, nome, cognome):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.nome == nome and cliente.cognome == cognome:
                        return cliente
                return None
        else:
            return None

    def ricercaUtilizzatoreCF(self, codiceFiscale):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.codiceFiscale == codiceFiscale:
                        return cliente
                return None
        else:
            return None

    def ricercaUtilizzatoreCodice(self, codice):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                return clienti.get(codice, None)
        else:
            return None

    def rimuoviCliente(self):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                del clienti[self.codice]
            with open('Dati/Clienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        self.rimuoviUtilizzatore()
        self.abbonamenti = []
        self.note = ""
        del self

