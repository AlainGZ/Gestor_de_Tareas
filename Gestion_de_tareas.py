"""
Author: Alain Gomez Zapata
Fecha: 20/12/2024
Nombre de Programa: Foro semana 7 de Estructura de Datos
"""

def gestionar_pila():
    pila_tareas = []
    cantidad = int(input("¿Cuántas tareas desea agregar a la pila? "))
    for _ in range(cantidad):
        tarea = input("Ingrese una tarea: ")
        pila_tareas.append(tarea)
    
    print("Pila inicial de tareas:", pila_tareas)
    while True:
        pop = input("¿Desea eliminar la última tarea? (si/no): ").strip().lower()
        if pop == "si" and pila_tareas:
            ultima_tarea = pila_tareas.pop()
            print("Última tarea eliminada:", ultima_tarea)
            print("Pila actual:", pila_tareas)
        elif pop == "no":
            break
        else:
            print("La pila está vacía o la opción no es válida.")
    print("Pila final de tareas:", pila_tareas)

# Ejemplo de Cola
def gestionar_cola():
    from collections import deque
    cola_tareas = deque()
    cantidad = int(input("¿Cuántas tareas desea agregar a la cola? "))
    for _ in range(cantidad):
        tarea = input("Ingrese una tarea: ")
        cola_tareas.append(tarea)
    
    print("Cola inicial de tareas:", cola_tareas)
    while True:
        dequeue = input("¿Desea eliminar la primera tarea? (si/no): ").strip().lower()
        if dequeue == "si" and cola_tareas:
            primera_tarea = cola_tareas.popleft()
            print("Primera tarea eliminada:", primera_tarea)
            print("Cola actual:", cola_tareas)
        elif dequeue == "no":
            break
        else:
            print("La cola está vacía o la opción no es válida.")
    print("Cola final de tareas:", cola_tareas)
    if cola_tareas:
        print("Primera tarea actual:", cola_tareas[0])
        print("Última tarea actual:", cola_tareas[-1])

# Menú para seleccionar estructura de datos
def menu():
    while True:
        print("\nSeleccione la estructura de datos que desea gestionar:")
        print("1. Pila")
        print("2. Cola")
        print("3. Salir")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            gestionar_pila()
        elif opcion == "2":
            gestionar_cola()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()