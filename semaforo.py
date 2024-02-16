semaforo = input("Che tempo fa? ")

neve = "nevica ed è notte"
pioggia = "piove e non è notte"
sereno = "ci sta il sole"

if semaforo == neve:
    print("Rosso")
elif semaforo == pioggia:
    print("Giallo")
elif semaforo == sereno:
    print("Verde")
else:
    print("Condizione non gestita")
