class ListaSpesa:
    def __init__(self):
        self.lista = {}

    def aggiungi_articolo(self, articolo):
        self.lista[articolo] = False

    def spunta_articolo(self, articolo):
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
mia_lista.aggiungi_articolo("pane")
mia_lista.aggiungi_articolo("latte")
mia_lista.aggiungi_articolo("uova")
mia_lista.spunta_articolo("pane")
mia_lista.mostra_lista()
mia_lista.cancella_lista()