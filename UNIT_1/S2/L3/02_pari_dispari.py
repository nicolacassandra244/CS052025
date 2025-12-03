try:
    numero =int(input("Inserisci un numero. Ti dirò se pari o dispari!: "))
except ValueError:
    print(f"Valore non valido. Devi inserire un numero.")
    exit()
    
    
if numero % 2 == 0:
    
    print(f"{numero} è PARI.")
    
else:
    print(f"{numero} è DISPARI.")


