# Código en desarrollo...
# Este código es para analizar los logs previamente procesados y guardados en el fichero "logs_limpio.csv"
# Modifique la ruta del fichero
import pandas as pd

# Cargar los datos del archivo CSV
df = pd.read_csv('D:\\Escuela\\4to\\Trazas\\logs_limpio.csv') # Modifique esta ruta con la ubicacion del fichero

# Funciones
eventos_unicos = df['Evento'].unique()
cantidad_eventos = len(eventos_unicos)

# Mostrar eventos
def mostrar_eventos(inicio, fin):
    for evento in eventos_unicos[inicio:fin]:
        print(evento)

# Mostrar registro completo dado un evento
def mostrar_registro_completo(evento):
    registro = df[df['Evento'] == evento].iloc[0]
    for columna, valor in registro.items():
        print(f'{columna}: {valor}')

# Menú interactivo
inicio = 0
fin = 15
while True:
    print("\nMenú:")
    print("1. Mostrar los 15 primeros eventos")
    print("2. Evento más ejecutado")
    print("3. Evento menos ejecutado")
    print("x. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        mostrar_eventos(inicio, fin)
        while True:
            print("\nSubmenú:")
            print("1. Mostrar 5 eventos más")
            print("2. Mostrar los 15 últimos eventos")
            print("3. Mostrar todos los eventos")
            print("z. Atrás")
            subopcion = input("Elige una opción: ")
            if subopcion == '1':
                inicio = fin
                fin += 5
                mostrar_eventos(inicio, fin)
            elif subopcion == '2':
                inicio = -15
                fin = None
                mostrar_eventos(inicio, fin)
            elif subopcion == '3':
                inicio = 0
                fin = None
                mostrar_eventos(inicio, fin)
            elif subopcion.lower() == 'z':
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
    elif opcion == '2':
        evento_mas_ejecutado = df['Evento'].value_counts().idxmax()
        print(f'El evento más ejecutado es: {evento_mas_ejecutado}')
        while True:
            print("\nSubmenú:")
            print("1. Mostrar registro completo")
            print("z. Atrás")
            subopcion = input("Elige una opción: ")
            if subopcion == '1':
                mostrar_registro_completo(evento_mas_ejecutado)
            elif subopcion.lower() == 'z':
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
    elif opcion == '3':
        evento_menos_ejecutado = df['Evento'].value_counts().idxmin()
        print(f'El evento menos ejecutado es: {evento_menos_ejecutado}')
        while True:
            print("\nSubmenú:")
            print("1. Mostrar registro completo")
            print("z. Atrás")
            subopcion = input("Elige una opción: ")
            if subopcion == '1':
                mostrar_registro_completo(evento_menos_ejecutado)
            elif subopcion.lower() == 'z':
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
    elif opcion.lower() == 'x':
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
