import pandas as pd

# Carga los datos del archivo CSV
df = pd.read_csv('D:\\Escuela\\4to\\Trazas\\logs.csv')

# Separa la columna 'Marca de tiempo' en horas, minutos y segundos
df[['Hora', 'Minuto', 'Segundo']] = df['Marca de tiempo'].str.split(':', expand=True)
6
# Separa los segundos en segundos y milisegundos
df[['Segundo', 'Milisegundo']] = df['Segundo'].str.split(',', expand=True)

# Elimina cualquier ':' al final del valor en el campo 'Nivel'
df['Nivel'] = df['Nivel'].str.rstrip(':')

# Elimina los corchetes en el campo 'Evento'
df['Evento'] = df['Evento'].str.replace('[', '').str.replace(']', '')

# Rellena los valores nulos en el campo 'Milisegundo' con 0
df['Milisegundo'] = df['Milisegundo'].fillna('0')

# Elimina la columna 'Marca de tiempo'
df = df.drop(columns=['Marca de tiempo'])

# Reorganiza las columnas en el orden deseado
df = df.reindex(columns=['Dia', 'Mes', 'Año', 'Hora', 'Minuto', 'Segundo', 'Milisegundo','AM-PM', 'Nivel', 'Evento', 'Descripcion'])

# Define una función para asignar AM o PM basado en la hora
def asignar_am_pm(row):
    if pd.isnull(row['AM-PM']):
        if int(row['Hora']) >= 12:
            return 'PM'
        else:
            return 'AM'
    else:
        return row['AM-PM']

# Aplica la función a cada fila en el DataFrame
df['AM-PM'] = df.apply(asignar_am_pm, axis=1)

# Guarda los datos limpios en un nuevo archivo CSV
df.to_csv('D:\\Escuela\\4to\\Trazas\\logs_limpio.csv', index=False)
