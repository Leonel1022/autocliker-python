import pyautogui
import time

# Número de veces que presionará la tecla
veces = 200
tecla = a

# Esperar 3 segundo antes de comenzar
time.sleep(3)

for _ in range(veces):
    pyautogui.press('tecla')
    time.sleep(0.1)
    # Pausa pequeña entre cada pulsación para evitar posibles errores

# Salida después de completar
print("Proceso completado.")
