def addition (elt, operande, elt1):
    operande = ["+", "-", "*", "/"]
    if operande == "+":
        print(elt + elt1)
    elif operande == "-":
        print(elt - elt1)
    elif operande == "*":
        print(elt * elt1)
    else:
        print(elt / elt1)