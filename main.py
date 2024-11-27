import logging

def main():
    logging.basicConfig(filename="log/logs.log", filemode="a", format="%(levelname)s -- %(message)s", level=logging.INFO)
    a = int(input("Inserisci il primo numero: "))
    b = int(input("Inserisci il secondo numero: "))

    if a == b:
        logging.info(f"I numeri sono identici")    
    else:
        max_value = max(a,b)
        logging.info(f"Il numero massimo tra i due: {max_value}")
  

if  __name__ == "__main__":
    main()