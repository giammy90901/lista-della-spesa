altezza = float(input("Inserisci l'altezza del visitatore in centimetri: "))
eta = int(input("Inserisci l'età del visitatore: "))

if altezza < 140 and eta < 18:
    print("Accesso negato. Il visitatore è troppo giovane e troppo basso per accedere alla giostra.")
elif altezza < 140 and eta >= 18:
    print("Accesso consentito con rialzo. Il visitatore è abbastanza alto ma troppo giovane per accedere alla giostra.")
else:
    print("Accesso consentito. Il visitatore può accedere alla giostra.")
