import random
import string

print("QUESTO PROGRAMMA GENERERÀ UNA PASSWORD PER TE") # PRESENTAZIONE DEL PROGRAMMA

print("Quanto vuoi che sia lunga la tua password? (Inserisci un numero intero)")

while True:
    lunghezza_input = input()
    try:
        # Tenta di convertire l'input in un intero
        lunghezza = int(lunghezza_input)

        # Controlla se il numero è positivo
        if lunghezza > 0:
            break  # Esci dal ciclo se è un intero positivo
        else:
            print("Per favore, inserisci un numero intero positivo:")
    except ValueError:
        # Cattura l'errore se l'input non è convertibile in intero
        print("Input non valido. Per favore, inserisci un numero intero:")

print(f"\nHai scelto una lunghezza di: {lunghezza}")

# Definisce l'insieme di tutti i caratteri possibili per la password
# Include lettere minuscole, maiuscole, cifre e simboli di punteggiatura.
caratteri = string.ascii_letters + string.digits + string.punctuation

# Genera la password
# 1. 'random.choice(caratteri)' seleziona un carattere casuale dalla stringa 'caratteri'.
# 2. Il ciclo 'for _ in range(lunghezza)' esegue l'operazione per la lunghezza desiderata.
# 3. La funzione '"".join(...)' unisce tutti i caratteri selezionati in un'unica stringa.
password = "".join(random.choice(caratteri) for _ in range(lunghezza))

print(f"La tua nuova password generata è: {password}")