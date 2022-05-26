import os.path
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from Attivita.Cliente import Cliente
from Viste.VistaCliente import VistaCliente
from Viste.VistaInserisciCliente import VistaInserisciCliente


class VistaGestisciClienti(QWidget):

    def __init__(self, parent=None):
        super(VistaGestisciClienti, self).__init__(parent)
        h_layout = QHBoxLayout()
        self.list_view = QListView()
        self.update_ui()
        h_layout.addWidget(self.list_view)

        buttons_layout = QVBoxLayout()
        open_button = QPushButton('Apri')
        open_button.clicked.connect(self.show_selected_info)
        buttons_layout.addWidget(open_button)

        new_button = QPushButton('Nuovo')
        new_button.clicked.connect(self.show_new)
        buttons_layout.addWidget(new_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle("Gestisci Clienti")

    def load_clienti(self):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.clienti.extend(current.values())

    def update_ui(self):
        self.clienti = []
        self.load_clienti()
        listview_model = QStandardItemModel(self.list_view)
        for cliente in self.clienti:
            item = QStandardItem()
            nome = f"{cliente.nome} {cliente.cognome} - {type(cliente).__name__} {cliente.codice}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.list_view.setModel(listview_model)

    def show_selected_info(self):
        try:
            selected = self.list_view.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            codice = int(selected.split("-")[1].strip().split(" ")[1])
            cliente = None
            if tipo == "Cliente":
                cliente = Cliente().ricercaUtilizzatoreCodice(codice)
            self.vista_cliente = VistaCliente(cliente, elimina_callback=self.update_ui)
            self.vista_cliente.show()
        except IndexError:
            print("INDEX ERROR")
            return

    def show_new(self):
        self.inserisci_cliente = VistaInserisciCliente(callback=self.update_ui)
        self.inserisci_cliente.show()
