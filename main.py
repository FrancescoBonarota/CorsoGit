import logging

def max_value(a, b):
    if a == b:
        logging.info(f"I numeri sono identici")    
    elif a > b:
        logging.info(f"Il numero massimo tra i due: {a}")    
    else:
        logging.info(f"Il numero massimo tra i due: {b}")    

def min_value(a, b):
    if a == b:
        logging.info(f"I numeri sono identici")    
    elif a < b:
        logging.info(f"Il numero minimo tra i due: {a}")    
    else:
        logging.info(f"Il numero minimo tra i due: {b}")    

def main():
    logging.basicConfig(filename="log/logs.log", filemode="a", format="%(levelname)s -- %(message)s", level=logging.DEBUG)
    a = int(input("Inserisci il primo numero: "))
    b = int(input("Inserisci il secondo numero: "))

    max_value(a, b)
    min_value(a, b)
    


if  __name__ == "__main__":
    main()