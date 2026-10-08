class Studente:
    def __init__(self, matricola, nome, cognome, data_nascita):
        self.matricola = matricola
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita

        @property
        def matricola(self):
            return self.matricola

        @matricola.setter
        def matricola(self, matricola):
            self.matricola = matricola

    def __str__(self):
        return f"{self.matricola} {self.nome} {self.cognome} {self.data_nascita}"