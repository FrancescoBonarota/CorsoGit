def main():
    a = int(input("Inserisci il primo numero: "))
    b = int(input("Inserisci il secondo numero: "))

    if a == b:
        print("I numeri sono identici")
    elif a > b:
        print("Il numero più grande tra i due è " + str(a))
    else:
        print("Il numero più grande tra i due è " + str(b))


if  __name__ == "__main__":
    main()