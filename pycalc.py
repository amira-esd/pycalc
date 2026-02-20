def calculatrice (elt, operande, elt1):

    if operande == "+":
        print(elt + elt1)
    elif operande == "-":
        print(elt - elt1)
    elif operande == "*":
        print(elt * elt1)
    else:
        print(elt / elt1)

calculatrice(5, "*", 5)
