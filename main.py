import utils
import console

if utils.check_for_ffmpeg() is False:
  print('ffmpeg no se encuentra instalado. Esta librería es necesaria para el correcto funcionamiento.')
  exit()
  
console.init()