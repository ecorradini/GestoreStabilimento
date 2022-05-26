from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

from Viste.VistaGestisciClienti import VistaGestisciClienti


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Gestisci Servizi", self.go_servizi), 0, 0)
        grid_layout.addWidget(self.get_generic_button("Gestisci Abbonamenti", self.go_abbonamenti), 0, 1)
        grid_layout.addWidget(self.get_generic_button("Gestisci Dipendenti", self.go_dipendenti), 1, 0)
        grid_layout.addWidget(self.get_generic_button("Gestisci Clienti", self.go_clienti), 1, 1)
        grid_layout.addWidget(self.get_generic_button("Gestisci Sistema", self.go_sistema), 2, 0, 1, 2)
        self.setLayout(grid_layout)
        self.resize(400, 300)
        self.setWindowTitle("Gestore Stabilimento PRO")

    def get_generic_button(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_servizi(self):
        pass

    def go_clienti(self):
        self.vista_gestisci_clienti = VistaGestisciClienti()
        self.vista_gestisci_clienti.show()

    def go_dipendenti(self):
        pass

    def go_abbonamenti(self):
        pass

    def go_sistema(self):
        pass