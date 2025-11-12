def addizione(x, y):
    """Restituisce la somma di due numeri."""
    return x + y

def sottrazione(x, y):
    """Restituisce la differenza tra due numeri."""
    return x - y

def moltiplicazione(x, y):
    """Restituisce il prodotto di due numeri."""
    return x * y

def divisione(x, y):
    """Restituisce la divisione tra due numeri, gestendo la divisione per zero."""
    if y == 0:
        # *Correzione: Per gestire l'errore matematico
        return "Errore: Divisione per zero non consentita!"
    return x / y

# ----------------------------------------------------------------------
# PROGRAMMA PRINCIPALE
# ----------------------------------------------------------------------

print("BENVENUTO NELLA CALCOLATRICE SEMPLICE")
print("Scegli un'operazione:")
print("1. Addizione")
print("2. Sottrazione")
print("3. Moltiplicazione")
print("4. Divisione")

while True:
    # Richiedi l'input dell'operazione
    scelta = input("Inserisci la scelta (1/2/3/4): ")

    # Controlla se la scelta è valida
    if scelta in ('1', '2', '3', '4'):
        try:
            # Richiedi i due numeri
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
        except ValueError:
            # *Correzione: Gestisce l'errore se l'input non è un numero
            print("Input non valido. Per favore, inserisci un numero.")
            continue # Ritorna all'inizio del ciclo

        if scelta == '1':
            risultato = addizione(num1, num2)
        elif scelta == '2':
            risultato = sottrazione(num1, num2)
        elif scelta == '3':
            risultato = moltiplicazione(num1, num2)
        elif scelta == '4':
            risultato = divisione(num1, num2)
        
        # Stampa il risultato
        print(f"\nIl risultato è: {risultato}\n")
        
        # Dopo il calcolo, chiedi se continuare o uscire
        next_calculation = input("Vuoi eseguire un altro calcolo? (sì/no): ")
        if next_calculation.lower() != 'sì' and next_calculation.lower() != 'si':
            break
    else:
        # *Correzione: Se l'utente non inserisce una scelta valida
        print("Scelta non valida. Inserisci un numero da 1 a 4.")

print("Calcolatrice chiusa. Arrivederci!")