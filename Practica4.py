Cal1= (int(input("Ingrese un numero: ")))
Cal2= (int(input("Ingrese otro numero: ")))
Cal3= (int(input("Ingrese un numero: ")))

CalT=(Cal1+Cal2+Cal3)/3


if CalT>=70:
    print("Aprobo")
elif 0<CalT<70:
    print("Reprobo")
else:
    print("Error")