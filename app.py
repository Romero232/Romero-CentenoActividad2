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

# Ejercicio 6: Implementar un Menú de Opciones
def mostrar_menu():
    print("1. Opción A")
    print("2. Opción B")
    print("3. Opción C")
    print("4. Salir")

def entrada_valida(opcion):
    return opcion.isdigit() and 1 <= int(opcion) <= 4

# Ejercicio 7: Verificar que la Entrada No Contenga Espacios
def entrada_sin_espacios(entrada):
    return ' ' not in entrada and not entrada.isspace()

# Ejercicio 8: Solicitar Varias Letras Separadas por Comas y Validar
def letras_validas(letras):
    letras = letras.split(',')
    letras = [letra.strip() for letra in letras]
    
    for letra in letras:
        if len(letra) != 1 or not letra.isalpha():
            return False, "Todas las entradas deben ser letras individuales."
    
    if len(letras) != len(set(letras)):
        return False, "No puede haber letras repetidas."
    
    return True, ""

# Ejercicio 9: Limitar el Número de Intentos de Entrada
def ingresar_letras():
    intentos = 0
    while intentos < 5:
        letras = input("Ingrese varias letras separadas por comas: ")
        if not entrada_sin_espacios(letras):
            print("La entrada no debe contener espacios. Intente de nuevo.")
        else:
            valido, mensaje = letras_validas(letras)
            if valido:
                print("Entrada válida:", letras)
                return
            else:
                print(mensaje)
        intentos += 1
    
    print("Número máximo de intentos alcanzado.")

# Ejercicio 10: Mensaje Personalizado según el Error de Validación
def main():
    while True:
        # Mostrar menú y recibir la opción del usuario
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        # Validar la opción seleccionada
        if not entrada_valida(opcion):
            print("Opción no válida. Intente de nuevo.")
            continue
        
        # Salir del programa
        if opcion == "4":
            print("Saliendo...")
            break

        # Llamar a la función para ingresar letras
        ingresar_letras()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
