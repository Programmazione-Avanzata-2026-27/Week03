
class Corso:
    def __init__(self, codice, titolo, docente):
        self.codice = codice
        self.titolo = titolo
        self.docente = docente

        self.lista_studenti = []

    def __str__(self):
        return f"{self.titolo} {self.codice} {self.docente}"