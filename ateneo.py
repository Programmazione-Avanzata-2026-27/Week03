# Per utilizzare classi definite in altri file/moduli devo prima importarle

from studente import Studente
from corso import Corso

def main():

    # Posso creare oggetti di tipo/classe Studente
    s1 = Studente("1234", "Mario", "Rossi", "20201014")

    print(s1) # Chiama automaticamente __str()__
    s2 = Studente("5678", "Gianni", "Blu", "20190715")

    # Posso memorizzare più studenti in una lista o altra struttura dati
    lista_studenti = [s1]
    lista_studenti.append(s2)

    # Posso creare oggetti di altri tipi, es. Corso
    c001 = Corso("001", "Programmazione avanzata", "Lamberti")



main()