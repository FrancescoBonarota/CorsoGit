import logging
import pandas as pd
import numpy

import pandas as pd

def compute_avg():
    """
    Questa funzione calcola la media voto di ogni studente
    """
    
    # crea un dataframe con i voti degli studenti
    students = {
    "francesco": [7, 8, 5, 6],
    "andrea": [8, 10, 7, 8],
    "gino": [5, 6, 6, 6],
    "lorenzo": [6, 7, 7, 8],
    "pino": [4, 4, 3, 4]
    }

    df_stud = pd.DataFrame(students, index = ["matematica", "informatica", "inglese", "italiano"])

    print(f"\n\nI voti per ogni studente in ogni materia: \n{df_stud}") 

    # Calcola la media dei voti per ogni studente
    avg_votes = df_stud.mean(axis=0)  # Calcola la media lungo le righe per ogni colonna
    
    print(f"\n\nLa media voto per ogni studente: \n{avg_votes.to_string()}")    



def max_numbers():
    """
    Questa funzione calcola il massimo tra due numeri inseriti in input 
    """

    logging.basicConfig(filename="log/logs.log", filemode="a", format="%(levelname)s -- %(message)s", level=logging.INFO)
    a = int(input("Inserisci il primo numero: "))
    b = int(input("Inserisci il secondo numero: "))

    if a == b:
        max_value = -1
        logging.info(f"I numeri sono identici")   
    else:
        max_value = max(a,b)
        logging.info(f"Il numero massimo tra i due: {max_value}")
        print((f"Il numero massimo tra i due: {max_value}"))

def main():

    cmd_func = input("Scegli la funzione da eseguire (max, avg): ")
    if cmd_func == "max":
        max_numbers()

    elif cmd_func == "avg":
        compute_avg()

    else:
        print("Devi scrivere max o avg")
  

if  __name__ == "__main__":
    main()
