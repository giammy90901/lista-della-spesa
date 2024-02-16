eta = int(input("Inserisci la tua età: "))

if eta >= 21:
    print("Sei maggiorenne e puoi votare.")
elif eta >= 18:
    print("puoi votare ma non sei magiorenne. ")
else:
    print("Sei minorenne e non puoi votare.")
