
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
from datetime import datetime, timedelta

# Configura la autenticación de Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Abre una ventana de autenticación en el navegador

# Inicia el objeto GoogleDrive
drive = GoogleDrive(gauth)

# ID de la carpeta de Google Drive que deseas descargar
folder_id = '1-77LjSpTs23DMr4k6zPE_MM6PJZwKQy8'

# Ruta local donde deseas guardar los archivos descargados
local_folder = 'C:/drive_local/'

# Calcula la fecha de inicio (hace un día desde hoy)
end_date = datetime.now()
start_date = end_date - timedelta(days=1)

# Convierte las fechas a formato ISO8601 para la consulta
start_date_iso = start_date.isoformat() + 'Z'
end_date_iso = end_date.isoformat() + 'Z'

# Consulta los archivos en la carpeta de Google Drive modificados entre las fechas
query = f"'{folder_id}' in parents and modifiedTime > '{start_date_iso}' and modifiedTime < '{end_date_iso}'  and title contains '.txt'"

# Obtiene la lista de archivos que cumplen con la consulta
file_list = drive.ListFile({'q': query}).GetList()

# Descarga los archivos a la carpeta local
for file1 in file_list:
    file1.GetContentFile(os.path.join(local_folder, file1['title']))

print(f"Se han descargado {len(file_list)} archivos desde Google Drive.")