#Rutina para generar los términos de la sucesión de fibonacci
a=int(input("Intruduzca hasta que posición de la sucesión quiere generar los términos: "))
print("")
def f(n):
    if n < 2:
        return 1
    else:
        return f(n-1) + f(n-2)
print("La lista de los términos de la sucesión hasta la posición pedida es:")
print("")
for x in range(a):
    print(f(x))

