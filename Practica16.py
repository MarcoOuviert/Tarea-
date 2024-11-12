sum=0
cont=1
while cont<=10:
    cont+=1
    num=int(input("Ingrese un numero: "))
    if 5<=num<=2500:
        sum=num+sum

print("La suma es: ", sum)
print("el promedio es: ", (sum/10))