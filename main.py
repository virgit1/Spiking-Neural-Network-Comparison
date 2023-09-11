import subprocess
import time

# Inicia el proceso que se va a medir
process = subprocess.Popen(['python', 'pruebagpu.py'])

# Espera a que el proceso se inicie completamente
time.sleep(5)

# Inicia la medición del consumo de energía de la GPU
nvidia_dmon = subprocess.Popen(['nvidia-smi', 'dmon', '-s', 'u'], stdout=subprocess.PIPE)

# Espera a que el proceso termine
process.wait()

# Detiene la medición del consumo de energía de la GPU
subprocess.Popen(['nvidia-smi', 'dmon', '-f', 'output.csv', '-s', 'p'], stdout=subprocess.PIPE)

# Mata los subprocesos
try:
    process.kill()
except OSError:
    pass

try:
    nvidia_dmon.kill()
except OSError:
    pass
