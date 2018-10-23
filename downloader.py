import youtube_dl
from colorama import init
from blessings import Terminal



# t = Terminal()

# ydl_only_audio_opts = {
#     'format': 'bestaudio/best',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }],
# }

# print(t.bold_yellow('Bienvenido! Este programa sirve para descargar videos de distintos lugares'))
# print(t.bold_yellow('Solo seguí las instrucciones!'))

# url = input(t.bold('Ingresa la URL (link) del video: '))

# username = input(t.bold('Usuario (En caso que tengas que logearte, ej: una playlist privada de YT, si no, dejalo en blanco: '))
# password = input(t.bold('Contraseña (Si no agregaste usuario, dejalo en blanco)'))

# video_name = input(t.bold('Nombre (dejalo en blanco para el default)'))

# only_audio = input(t.bold('Solo audio? (s/n)'))

# if video_name is '':
#     video_name = '%(id)s%(ext)s'

# if only_audio is 's':

# with ydl:
#     result = ydl.extract_info(url)

# if 'entries' in result:
#     # Can be a playlist or a list of videos
#     video = result['entries'][3]
# else:
#     # Just a video
#     video = result

# print(video)
# video_url = video['webpage_url']
# print(video_url)