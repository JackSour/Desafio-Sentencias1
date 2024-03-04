
import sys

# Tratamiento de datos ingresados
peso = float(sys.argv[1]) 
altura_ctms = float(sys.argv[2])

# Conversion altura de ctms a mts
altura = altura_ctms/100

# Formula calculo imc
imc = (peso/(altura ** 2))

#Mostrar resultado de IMC
print(f"Su IMC es {imc:.2f}")

# Clasificacion he impresion de IMC
if imc < 18.5:
    print("La clasificación OMS es Bajo Peso")
elif 18.5 <= imc < 25:
    print("La clasificación OMS es Adecuado")
elif 25 <= imc < 30:
    print("La clasificación OMS es Sobrepeso")
elif 30 <= imc < 35:
    print("La clasificación OMS es Obesidad Grado I")
elif 35 <= imc < 40:
    print("La clasificación OMS es Obesidad Grado II")
else:
    print("La clasificación OMS es Obesidad Grado III")
