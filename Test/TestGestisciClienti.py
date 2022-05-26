import datetime
import os.path
import pickle
from unittest import TestCase

from Attivita.Cliente import Cliente


class TestGestioneCliente(TestCase):

    def test_add_cliente(self):
        self.cliente = Cliente()
        self.cliente.aggiungiCliente("note", [], 123, "Test", "Test", datetime.datetime(1989, 10, 20), "prova",
                                     "prova", 1)
        clienti = None
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        self.assertIsNotNone(clienti)
        self.assertIn(1, clienti)

    def test_rimuovi_cliente(self):
        clienti = None
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        self.assertIsNotNone(clienti)
        self.assertIn(1, clienti)
        self.cliente = Cliente().ricercaUtilizzatoreCodice(1)
        self.cliente.rimuoviCliente()
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        self.assertIsNotNone(clienti)
        self.assertNotIn(1, clienti)
