try:
    numero1 = int(input("Inserisci il primo numero: "))
    numero2 = int(input("Inserisci il secondo numero: "))
    numero3 = int(input("Inserisci il terzo numero:"))



except ValueError:
    print(f"Valore non valido. Devi inserire un numero.")
    exit()


somma = numero1 + numero2 + numero3
media = somma / 3

print(f"La media è {media}")