# 1. Bienvenida
def bienvenida():
    print("""
    *******************************
    *  CALCULADORA DE PROMEDIO   *
    *******************************
    """)

# 2. Función para ingresar notas
def ingresar_notas():
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i}: "))
                if 0 <= nota <= 20:
                    notas.append(nota)
                    break
                else:
                    print("❌ La nota debe estar entre 0 y 20")
            except ValueError:
                print("❌ Ingresa un número válido")
    return notas

# 3. Función para calcular promedio
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# 4. Función principal
def main():
    bienvenida()
    notas = ingresar_notas()
    promedio = calcular_promedio(notas)
    
    print("\n----- RESULTADOS -----")
    for i, nota in enumerate(notas, start=1):
        print(f"Nota {i}: {nota}")
    print(f"\nPromedio final: {promedio:.2f}")
    
    if promedio >= 11:
        print("✅ ¡Aprobaste!")
    else:
        print("❌ Lo siento, desaprobaste.")

# 5. Ejecutar
if __name__ == "__main__":
    main()

