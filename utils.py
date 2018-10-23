import subprocess

def check_for_ffmpeg():
  cp = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
  return_code = cp.returncode
  
  if return_code is not 0:
    return False
  else:
    return True
