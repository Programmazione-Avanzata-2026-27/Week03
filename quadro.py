class Quadro:
    # Metodo/Funzione che costruisce gli oggetti di classe Quadro e li inizializza
    def __init__(self, artista, titolo, materiali, anno):
        self.__artista = artista # Privati/Nascosti (con _ per scoraggiare o __ per bloccare l'accesso)
        self.__titolo = titolo
        self.__materiali = materiali
        self.__anno = anno #1853 e 1890

    # Altri metodi, es. getter/setter per l'accesso agli attrributi in lettura e scrittura

    # Metodo per leggere il valore dell'attributo nascosto anno (metodo getter)
    @property
    def anno(self):
        return self.__anno

    # Metodo per impostare il valore dell'attributo nascosto anno (metodo setter)
    @anno.setter
    def anno(self, anno):
        self.__anno = anno # Eventualmente posso aggiungere codice per controllo errori

    # Metodo/Funzione che consente al quadro di descriversi come stringa
    # __str__ come alternativa a nomi più bizzarri come descriviti(), ...
    def __str__(self):
        return f"{self.__artista}, {self.__titolo}, {self.__materiali}, {self.__anno}"



q1 = Quadro("Van Gogh", "Autoritratto", "Olio su tela", 1870)

#print(f"{q1.__artista} {q1.__titolo} {q1.__materiali} {q1.__anno}")

# q1.__anno = 1945 # Non posso farlo così perché l'attributo è privato/nascosto

# Per accedere all'attributo devo usare i metodi/le funzioni

# q1.imposta_anno(1800)

#print(f"{q1.__artista} {q1.__titolo} {q1.__materiali} {q1.__anno}")

# print("Anno:"+str(q1.leggi_anno()))

print("Anno: " + str(q1.anno))

# Come faccio a stampare il quadro

print(q1)

# print(q1.__artista)

# Chi meglio del quadro sa come stamparsi?

# print(q1.descriviti()) # Ho DELEGATO al quadro il compito di stamparsi

print(q1.__str__())


