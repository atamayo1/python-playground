def ingresar_calificaciones():
    """
    Solicita al usuario materias y calificaciones.
    Devuelve dos listas paralelas:
    - nombres_materias
    - calificaciones
    """
    nombres_materias = []
    calificaciones = []

    while True:
        nombre = input("Introduce el nombre de la materia: ")

        # Validación de calificación
        while True:
            try:
                nota = float(input("Introduce la calificación (0 a 10): "))
                if 0 <= nota <= 10:
                    break
                else:
                    print("Debe estar entre 0 y 10.")
            except ValueError:
                print("Ingrese solo números.")

        nombres_materias.append(nombre)
        calificaciones.append(nota)

        continuar = input("¿Agregar otra materia? (s/n): ").lower()
        if continuar != "s":
            break

    return nombres_materias, calificaciones


def calcular_promedio(calificaciones):
    """
    Calcula promedio usando funciones básicas.
    Maneja lista vacía.
    """
    if len(calificaciones) == 0:
        return None

    suma = 0
    for calificacion in calificaciones:
        suma += calificacion

    return suma / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """
    Devuelve dos listas:
    - índices de aprobados
    - índices de reprobados
    """
    aprobados = []
    reprobados = []

    for i in range(len(calificaciones)):
        if calificaciones[i] >= umbral:
            aprobados.append(i)
        else:
            reprobados.append(i)

    return aprobados, reprobados


def encontrar_extremos(calificaciones):
    """
    Devuelve índices de:
    - calificación más alta
    - calificación más baja
    """
    if len(calificaciones) == 0:
        return None, None

    indice_max = 0
    indice_min = 0

    for i in range(1, len(calificaciones)):
        if calificaciones[i] > calificaciones[indice_max]:
            indice_max = i
        if calificaciones[i] < calificaciones[indice_min]:
            indice_min = i

    return indice_max, indice_min


def main():
    nombres, notas = ingresar_calificaciones()

    if len(notas) == 0:
        print("⚠ No se ingresaron materias.")
        return

    promedio = calcular_promedio(notas)
    print(f"Promedio: {promedio:.2f}")

    aprobados, reprobados = determinar_estado(notas)

    print("Materias aprobadas:")
    for i in aprobados:
        print("-", nombres[i], notas[i])

    print("Materias reprobadas:")
    for i in reprobados:
        print("-", nombres[i], notas[i])

    i_max, i_min = encontrar_extremos(notas)

    print("Mejor calificación:")
    print(nombres[i_max], notas[i_max])

    print("Peor calificación:")
    print(nombres[i_min], notas[i_min])


if __name__ == "__main__":
    main()
