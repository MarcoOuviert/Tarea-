
alumnos=[]
for i in range(24):

    Nombre=input("Ingrese su nombre: ")
    Apellido=input("Ingrese su apellido: ")
    Cal=int(input("Ingrse su calificacion: "))
    alumno= (Nombre, Apellido, Cal)
    alumnos.append(alumno)

print ("Lista de alumnos")

for alumno in alumnos:
    Nombre,Apellido,Cal= alumno
    print(f'El alumno{Nombre} {Apellido} tiene una calificacion de: {Cal}')