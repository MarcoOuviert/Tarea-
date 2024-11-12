for i in range (100):
    num=int(input("Ingrese un numero: "))
    if num==0:
        print("El numero es igual a 0")
    elif num<0:
        print("El numero es negativo")
    elif 0<num<10:
        print("El numero esta entre 0 y 10")
    elif num==100:
        print("El numero es igual a 100")
    elif 10<num<100:
        print("El numero esta entre 10 y 100")
   