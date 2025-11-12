import os
import sys

def leggi_e_stampa_file():
    """
    Chiede all'utente il nome di un file, lo cerca nella directory del programma,
    lo apre e ne stampa il contenuto.
    """
    print("--- LETTORE DI FILE DI TESTO ---")
    
    # 1. Ottiene il percorso della directory del programma
    # *Correzione: Ottiene il percorso assoluto del file .py che sta girando
    if getattr(sys, 'frozen', False):
        # Se l'eseguibile è stato 'freezato' (es. con PyInstaller)
        program_dir = os.path.dirname(sys.executable)
    else:
        # Percorso normale del file Python
        program_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Chiede all'utente il nome del file che vuole leggere
    nome_file_richiesto = input("Inserisci il nome del file di testo (es. miofile.txt): ")

    # 2. Costruisce il percorso completo del file
    # *Correzione: Unisce il percorso della directory con il nome del file
    percorso_completo = os.path.join(program_dir, nome_file_richiesto)
    
    print(f"Sto cercando il file in: {percorso_completo}")

    try:
        # Tenta di aprire il file usando il percorso completo
        # *Correzione: Utilizza la variabile 'percorso_completo'
        with open(percorso_completo, 'r', encoding='utf-8') as file:
            # Legge l'intero contenuto del file
            contenuto = file.read()
            
            print(f"\n--- Contenuto del file '{nome_file_richiesto}' ---\n")
            print(contenuto)
            print("\n------------------------------------")
            
    except FileNotFoundError:
        # Gestisce l'errore se il file non viene trovato
        print(f"\n*ERRORE: Il file '{nome_file_richiesto}' non è stato trovato nel percorso del programma.")
        print(f"Directory del programma: {program_dir}")
        
    except Exception as e:
        # Gestisce eventuali altri errori
        print(f"\n*ERRORE Generico durante la lettura del file: {e}")

# Avvia la funzione
leggi_e_stampa_file()