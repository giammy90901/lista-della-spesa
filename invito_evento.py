
eta = int(input("Quanti anni hai? "))
invito = input("Hai un invito? (sì/no): ").lower()
maggiorenne = 18


if maggiorenne <= eta and invito == "si":
    print("Puoi entrare!")
else:

    vip = input("Sei un cliente VIP? (sì/no): ").lower()

    if vip == "si":
        print("Puoi entrare come cliente VIP!")
    else:
        print("Mi dispiace, non puoi entrare.")
