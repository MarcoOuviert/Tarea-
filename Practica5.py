Sueldo=int(input("Ingrese su salario: "))
Years= int(input("Ingrese su antiguedad: "))
porcentaje=0

if Years>=5:
    porcentaje=0.50
elif Years<5:
    porcentaje=0.30
    
print("Su salario a conbrar es de: ", ((Sueldo*porcentaje)+Sueldo))
