a = 2
suma = 0
while a > 0:
    a = int(input("Digite un numero entero positivo o uno negativo para terminar: "))
    if a > 0 and a % 2 == 0:
        suma += a
print(suma)