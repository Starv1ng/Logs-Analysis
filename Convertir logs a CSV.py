# Modifique las rutas de la entrada de logs con la ubicacion de las carpetas donde se encuentran los logs
# Modifique la ruta donde desea guardar el CSV

import csv
import re
import os
#Procesar Alfresco y Excriba
def parse_log1(log_line):
    match = re.match(r'(\d{2}:\d{2}:\d{2},\d{3}) (\S+)  (\[.*?\]) (.*)', log_line)
    if match:
        hora, nivel, evento, descripcion = match.groups()
        dia, mes, año = None, None, None
        am_pm = None
    else:
        return None
    return dia, mes, año, hora, am_pm, nivel, evento, descripcion

import re
# Procesar Catalina
def parse_log2(log_lines):
    match1 = re.match(r'(\S+ \d{2}, \d{4} \d{1,2}:\d{2}:\d{2} \S+) (\S+)', log_lines[0])
    match2 = re.match(r'(\S+) (.*)', log_lines[1])
    if match1 and match2:
        marca_tiempo, nivel = match1.groups()
        evento, descripcion = match2.groups()
        dia, mes, año = marca_tiempo.split(' ')[0], marca_tiempo.split(' ')[1].replace(',', ''), marca_tiempo.split(' ')[2]
        hora = marca_tiempo.split(' ')[3]
        am_pm = marca_tiempo.split(' ')[4]
    else:
        return None
    return dia, mes, año, hora, am_pm, evento, nivel, descripcion
# Convertir a CSV
def convert_logs_to_csv(log_directories, csv_file_path):
    fieldnames = ['Dia', 'Mes', 'Año', 'Marca de tiempo', 'AM-PM', 'Nivel', 'Evento', 'Descripcion']

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for log_directory in log_directories:
            for log_file_name in os.listdir(log_directory):
                log_file_path = os.path.join(log_directory, log_file_name)
                with open(log_file_path, 'r', encoding='utf-8') as log_file:
                    logs = log_file.readlines()
                    i = 0
                    while i < len(logs):
                        parsed_log = None
                        if 'alfresco' in log_file_path or 'excriba' in log_file_path:
                            parsed_log = parse_log1(logs[i])
                            if parsed_log is not None:
                                dia, mes, año, hora, am_pm, nivel, evento, descripcion = parsed_log
                                writer.writerow({'Dia': dia, 'Mes': mes, 'Año': año, 'Marca de tiempo': hora, 'AM-PM': am_pm, 'Nivel': nivel, 'Evento': evento, 'Descripcion': descripcion})
                            i += 1
                        elif 'catalina' in log_file_path and i+1 < len(logs):
                            parsed_log = parse_log2([logs[i], logs[i+1]])
                            if parsed_log is not None:
                                dia, mes, año, hora, am_pm, nivel, evento, descripcion = parsed_log
                                writer.writerow({'Dia': dia, 'Mes': mes, 'Año': año, 'Marca de tiempo': hora, 'AM-PM': am_pm, 'Nivel': nivel, 'Evento': evento, 'Descripcion': descripcion})
                            i += 2
# Entrada de logs
# separar los logs de alfresco, excriba y catalina por carpetas
log_directories = ["D:\\Escuela\\4to\\Trazas\\logs\\logs\\alfresco", "D:\\Escuela\\4to\\Trazas\\logs\\logs\\excriba", "D:\\Escuela\\4to\\Trazas\\logs\\logs\\catalina"]
# Guardar los logs en un CSV
convert_logs_to_csv(log_directories, 'D:\\Escuela\\4to\\Trazas\\logs1.csv') # Modifique esta ruta con la ubicacion donde desea guardar el CSV
print("Done")
