from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from Attivita.Cliente import Cliente


class VistaCliente(QWidget):
    def __init__(self, cliente, elimina_callback):
        super(VistaCliente, self).__init__()
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()
        nome = ""
        info = {}
        if isinstance(cliente, Cliente):
            nome = f"Cliente {cliente.codice}"
            info = cliente.getInfoCliente()
        label_nome = QLabel(nome)
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        v_layout.addWidget(QLabel(f"Nome: {info['nome']}"))
        v_layout.addWidget(QLabel(f"Cognome: {info['cognome']}"))
        v_layout.addWidget(QLabel(f"Data nascita: {info['dataNascita']}"))
        v_layout.addWidget(QLabel(f"Codice Fiscale: {info['codiceFiscale']}"))
        v_layout.addWidget(QLabel(f"Email: {info['email']}"))
        v_layout.addWidget(QLabel(f"Telefonoo: {info['telefono']}"))

        if "note" in info:
            v_layout.addWidget(QLabel(f"Note: {info['note']}"))
        if "abbonamenti" in info:
            abbonamenti_attivi = [a for a in info['abbonamenti'] if not a.verificaScaduto()]
            v_layout.addWidget(QLabel(f"Abbonamenti attivi: {len(abbonamenti_attivi)}"))
            if len(abbonamenti_attivi) > 0:
                v_layout.addWidget(QLabel(f"Scadenza ultimo: {abbonamenti_attivi[len(abbonamenti_attivi)-1].dataScadenza}"))

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        btn_elimina = QPushButton('Elimina')
        btn_elimina.clicked.connect(lambda: self.elimina_cliente_click(cliente))
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.setWindowTitle("Cliente")

    def elimina_cliente_click(self, cliente):
        if isinstance(cliente, Cliente):
            cliente.rimuoviCliente()
        self.elimina_callback()
        self.close()
