# Ejercicio 1: Solicitar una Letra y Convertirla a Minúscula
letra = input("Introduce una letra: ")
letra = letra.lower()
print(f"Letra en minúscula: {letra}")

# Ejercicio 2: Validar que la Entrada No Sea un Número
if letra.isalpha():
    print(f"La letra es válida: {letra}")  
else:
    print("Error: Debe ingresar solo letras.")


# Ejercicio 3: Contar Intentos de Entrada Inválida
contador_intentos = 0

while True:
    letra = input("Introduce una letra: ").lower()
    if letra.isalpha():
        print(f"Letra válida: {letra}")
        break
    else:
        contador_intentos += 1
        print("Error: Debe ingresar solo letras.")
        print(f"Número de intentos inválidos: {contador_intentos}")

# Ejercicio 4: Crear una Función de Validación
def validar_letra():
    contador = 0
    while True:
        letra = input("Introduce una letra: ").lower()
        if letra.isalpha():
            return letra
        else:
            contador += 1
            print("Error: Debe ingresar solo letras.")
            print(f"Número de intentos inválidos: {contador}")

letra_valida = validar_letra()
print(f"Letra válida: {letra_valida}")

# Ejercicio 5: Validar que la Letra Pertenece al Alfabeto Español
def validar_letra_espanol():
    contador = 0
    while True:
        letra = input("Introduce una letra (alfabeto español): ").lower()
        if letra.isalpha() and len(letra) == 1:
            return letra
        else:
            contador += 1
            print("Error: Debe ingresar solo una letra del alfabeto español.")
            print(f"Número de intentos inválidos: {contador}")

letra_espanol = validar_letra_espanol()
print(f"Letra válida en español: {letra_espanol}")
