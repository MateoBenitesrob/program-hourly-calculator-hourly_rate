import time

nombre = input("Nombre del empleado: ")
if nombre.isalpha():
    time.sleep(1)
else:
    print("Nombre incorrecto. Ingrese letras.")
    exit()
time.sleep(2)

horas = input("Escriba el número de horas trabajadas al día: ")
if horas.isdigit():
    horas = int(horas)
    time.sleep(2)
else:
    print("ingrese solo el número de horas al día")
    exit()

pago_hora = (input("Escriba el pago por hora: "))
if pago_hora.isdigit():

    pago_hora = int(pago_hora)
    time.sleep(0.4)

else:
    print("Ingrese solo números")



# Sueldo por día
sueldo = horas * pago_hora
if sueldo > 50:
    print("Empleado con sueldo alto.")
    print("Su sueldo total al día es de", sueldo)
else:
    print("su sueldo total al día es de", sueldo)