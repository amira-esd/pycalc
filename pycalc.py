def calculatrice ():
    
    operation1 = int(input("Entrez un nombre : "))
    operation2 = str(input("Entrez un opérateur : "))
    operation3 = int(input("Entrez un nombre : "))

    if operation2 == "+" :
        print(operation1 + operation3)
    elif operation2 == "-":
        print(operation1 - operation3)
    elif operation2 == "*":
        i = 0
        total = 0
        while i <operation3:
            total+=operation1
            i+=1
        print(total)
    else:
        print(operation1 / operation3)

calculatrice()


