#convertir Salario en COP a USD

# creamos la función ConvertirAUsd que recibe el salario en COP, la tasa de cambio y realiza la conversión
# devuelve el salario en USD
def ConvertirAUsd(salarioCop, tasaCambio):
    conversion = salarioCop / tasaCambio
    return conversion

salario= int(input("Ingrese su salario en COP: "))
tasa= int(input("Ingrese la tasa de cambio COP/USD: "))

#enviamos el salario en COP y la tasa de cambio a la función ConvertirAUsd
salarioEnUsd = ConvertirAUsd(salario, tasa)

#imprimimos el resultado
print("El salario en USD es: ", salarioEnUsd)

