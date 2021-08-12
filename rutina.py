#Rutina para generar los términos de la sucesión del problema
a=int(input("Intruduzca hasta que posición de la sucesión quiere generar los términos: "))
print("")
def f(k):
    if k>0:
        g=(3*f(k-1))**(1/2)
        print(g)
    else:
        g=1
    return g
print("La lista de los términos de la sucesión hasta la posición pedida es:")
print("")
f(a)