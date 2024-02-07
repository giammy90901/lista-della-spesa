class ListaSpesa:
    def __init__(self):
        self.lista = {}

    def aggiungi_articolo(self):
        articolo = input("Inserisci l'articolo che vuoi aggiungere: ")
        self.lista[articolo] = False

    def spunta_articolo(self):
        articolo = input("Inserisci l'articolo che hai acquistato: ")
        if articolo in self.lista:
            self.lista[articolo] = True

    def mostra_lista(self):
        for articolo, spuntato in self.lista.items():
            stato = "Acquistato" if spuntato else "Da acquistare"
            print(f"{articolo}: {stato}")

    def cancella_lista(self):
        if all(self.lista.values()):
            self.lista.clear()
            print("La lista è stata cancellata.")
        else:
            print("Ci sono ancora articoli da acquistare.")

mia_lista = ListaSpesa()

while True:
    print("\n1. Aggiungi articolo")
    print("2. Spunta articolo")
    print("3. Mostra lista")
    print("4. Cancella lista")
    print("5. Esci")
    scelta = input("Scegli un'opzione: ")

    if scelta == '1':
        mia_lista.aggiungi_articolo()
    elif scelta == '2':
        mia_lista.spunta_articolo()
    elif scelta == '3':
        mia_lista.mostra_lista()
    elif scelta == '4':
        mia_lista.cancella_lista()
    elif scelta == '5':
        break
    else:
        print("Opzione non valida. Riprova.")
