
def calculaIMC(p,a):
    return p/ (a*a)

def nivelDePeso(IMC):
    if IMC < 18.5:
        return "Bajo Peso"
    elif 18.5 <= IMC <=24.9:
        return "Peso Normal"
    elif 25 <= IMC <= 29.9:
        return "Sobrepeso"
    elif 30 <= IMC <= 34.9:
        return "Obesidad I"
    elif 35 <= IMC <= 39.9:
        return "Obesidad II"
    elif 40 <= IMC <= 49.9:
        return "Obesidad III"
    elif IMC > 50:
        return "Obesidad IV"

nombre = input("Ingrese su nombre y apellido: ")
peso = float(input("Ingresa tu peso [kg]: "))
altura = float(input("Ingresa tu altura [m]: "))

indice = calculaIMC(peso, altura)
print(f"El indice de masa corporal de {nombre} es de: {indice}")

persona= nivelDePeso(indice)
print(f"El nivel de peso de {nombre} es: {persona}")