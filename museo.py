# Se voglio utilizzare una classe definita in un altro file (o modulo) devo
# usare le parole chiave import e from, importando es. la classe Quadro da quadro
from quadro import Quadro

# Ora posso utilizzare la classe Quadro, es. per creare oggetti
q = Quadro("Monet", "...", "...", "...")

print(q.__str__()) # Posso stampare l'oggetto chiedendo a quest'ultimo di restituire
                   # la sua descrizione come stringa con il metodo __str()__

print(q) # Se ho definito la funzione __str()__ per l'oggetto, quando
         # lo vado a stampare Python capisce che deve utilizzare quella
         # funzione anziché stampare l'indirizzo memoria, così non serve
         # neanche esplicitare .__str()__, viene invocata automaticamente

# Una volta definito un nuovo tipo di dato (il Quadro), posso creare delle
# collezioni di oggetti di quel tipo, esempio una lista

lista_di_quadri = []
lista_di_quadri.append(q)
lista_di_quadri.append(Quadro("Cezanne", "...", "...", "..."))
lista_di_quadri.append(Quadro("Pollock", "...", "...", "..."))

# Posso anche stampare il contenuto della lista, trattandola come un contenitore

print("Lista di quadri:")
for quadro in lista_di_quadri:
    print(quadro.__str__())

# 1. CON LE CLASSI POSSO DEFINIRE I MIEI TIPI DI DATO (ES. QUADRO)
# 2. POSSO DOTARLI DEI DATI/DEGLI ATTRIBUTI CHE LI CARATTERIZZNO (TENDENZIALMENTE NASCOSTI)
# 3. POSSO DOTARLI DELLE FUNZIONI/DEI METODI PER OPERARE SU QUEI DATI
#    OVVERO METODI GETTER/SETTER (PER ACCEDERE AGLI ATTRIBUTI) O ALTRI (ES. __str__())