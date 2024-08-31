import pyautogui
import time

# Número de veces que presionará la tecla Espacio
veces = 200

# Esperar 3 segundo antes de comenzar
time.sleep(3)

for _ in range(veces):
    pyautogui.press('space')
    # time.sleep(0.00001)  # Pausa pequeña entre cada pulsación para evitar posibles errores

# Salida después de completar
print("Proceso completado.")
