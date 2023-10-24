from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Autenticación
gauth = GoogleAuth()

# Intenta cargar las credenciales desde un archivo previamente guardado
gauth.LoadCredentialsFile("mycreds.txt")

# Si no hay credenciales almacenadas o están vencidas, inicia el proceso de autenticación
if gauth.credentials is None:
    # Abre una ventana del navegador para autenticación
    gauth.LocalWebserverAuth()

    # Guarda las credenciales en un archivo para su uso futuro
    gauth.SaveCredentialsFile("mycreds.txt")
elif gauth.access_token_expired:
    # Si las credenciales están vencidas, refresca el token
    gauth.Refresh()
else:
    # Si las credenciales son válidas, simplemente inicializa la autenticación
    gauth.Authorize()

# Crea una instancia de GoogleDrive
drive = GoogleDrive(gauth)


# ID de la carpeta de Google Drive que deseas acceder
folder_id = '1-77LjSpTs23DMr4k6zPE_MM6PJZwKQy8'

# Obtén la lista de archivos en la carpeta
# folder = drive.CreateFile({'id': folder_id})
file_list = drive.ListFile({'q': "'{}' in parents and trashed=false and title contains '.txt'".format(folder_id)}).GetList()

# Ruta local donde se descargarán los archivos
download_path = 'C:/drive_local/'

# Descarga los archivos en la carpeta
for file in file_list:
    file.GetContentFile(download_path + file['title'])

print(f'Se han descargado {len(file_list)} archivos en {download_path}')