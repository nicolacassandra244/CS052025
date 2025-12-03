
while True:
    try:
        numero = int(input("Inserisci un numero, ti calcolerò la tabellina!: "))
        break
    except ValueError:
        print(f"Valore non valido. Prova di nuovo: ")
print("---Tabellina---")
for moltiplicatore in range(0,11):
    risultato = numero * moltiplicatore
    print(f"{numero} * {moltiplicatore} = {risultato}")