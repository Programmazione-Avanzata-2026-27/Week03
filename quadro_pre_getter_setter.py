
class Quadro:
    def __init__(self, artista, titolo, materiali, anno):
        self.__artista = artista # Proteggo/nascondo l'accesso agli attributi, con __
        self.__titolo = titolo
        self.__materiali = materiali
        self.__anno = anno

    # Posso poi definire dei metodi per accedere agli attributi, es. per l'anno

    # Per ora uso questi nomi, anche se ce ne sono di migliori (getter/setter)
    def imposta_anno(self, nuovo_anno):
        if(nuovo_anno>1853 and nuovo_anno<1890): # Così posso anche effettuare controlli su possibili errori
            self.__anno = nuovo_anno
        else:
            print("L'anno inserito non è valido")

    def leggi_anno(self):
        return self.__anno

# q1 = Quadro("Van Gogh", "Autoritratto", "Olio su tela", 1870)

#print(f"{q1.__artista} {q1.__titolo} {q1.__materiali} {q1.__anno}")

# q1.__anno = 1945 # Non posso (più) accedervi così perché l'attributo è protetto/nascosto

# Ora, per accedere all'attributo, devo usare i metodi/le funzioni

# Esempio, per acccedere in scrittura

# q1.imposta_anno(1800)

# Idem in lettura

# print("Anno:"+str(q1.leggi_anno()))
