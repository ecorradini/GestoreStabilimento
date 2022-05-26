import os.path
import pickle

from Attivita.Utilizzatore import Utilizzatore

class Bagnino(Utilizzatore):

    def __init__(self):
        super().__init__()
        self.licenza = ""
        self.nazionalita = ""

    def aggiungiBagnino(self, licenza, nazionalita, nome, telefono, email, cognome, dataNascita, codiceFiscale, codice):
        self.aggiungiUtilizzatore(telefono=telefono, nome=nome, email=email,
                                  dataNascita=dataNascita, cognome=cognome, codiceFiscale=codiceFiscale,
                                  codice=codice)
        self.licenza = licenza
        self.nazionalita = nazionalita
        bagnini = {}
        if os.path.isfile('Dati/Bagnini.pickle'):
            with open('Dati/Bagnini.pickle', 'rb') as f:
                bagnini = pickle.load(f)
        bagnini[codice] = self
        with open('Dati/Bagnini.pickle', 'wb') as f:
            pickle.dump(bagnini, f, pickle.HIGHEST_PROTOCOL)

    def getInfoBagnino(self):
        info = self.getInfoUtilizzatore()
        info["licenza"] = self.licenza
        info["nazionalita"] = self.nazionalita
        return info

    def ricercaUtilizzatoreNomeCognome(self, nome, cognome):
        if os.path.isfile('Dati/Bagnini.pickle'):
            with open('Dati/Bagnini.pickle', 'rb') as f:
                bagnini = dict(pickle.load(f))
                for bagnino in bagnini.values():
                    if bagnino.nome == nome and bagnino.cognome == cognome:
                        return bagnino
                return None
        else:
            return None

    def ricercaUtilizzatoreCF(self, codiceFiscale):
        if os.path.isfile('Dati/Bagnini.pickle'):
            with open('Dati/Bagnini.pickle', 'rb') as f:
                bagnini = dict(pickle.load(f))
                for bagnino in bagnini.values():
                    if bagnino.codiceFiscale == codiceFiscale:
                        return bagnino
                return None
        else:
            return None

    def ricercaUtilizzatoreCodice(self, codice):
        if os.path.isfile('Dati/Bagnini.pickle'):
            with open('Dati/Bagnini.pickle', 'rb') as f:
                bagnini = dict(pickle.load(f))
                return bagnini.get(codice, None)
        else:
            return None

    def rimuoviBagnino(self):
        if os.path.isfile('Dati/Bagnini.pickle'):
            with open('Dati/Bagnini.pickle', 'wb+') as f:
                bagnini = dict(pickle.load(f))
                del bagnini[self.codice]
                pickle.dump(bagnini, f, pickle.HIGHEST_PROTOCOL)
        self.rimuoviUtilizzatore()
        self.licenza = ""
        self.nazionalita = ""
        del self

