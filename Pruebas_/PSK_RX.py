import numpy as np
import sounddevice as sd

# Parámetros de la demodulación PSK
frecuencia_portadora = 4000  # Frecuencia de la portadora en Hz
tasa_muestreo = 44100  # Tasa de muestreo en muestras por segundo
bits_por_simbolo = 1  # Número de bits por símbolo (PSK binaria)
duración_símbolo = 0.1  # Duración de cada símbolo en segundos

# Capturar audio del micrófono
duración_captura = duración_símbolo * bits_por_simbolo  # Duración de la captura en segundos
muestras_capturadas = int(duración_captura * tasa_muestreo)
captura_audio = sd.rec(muestras_capturadas, samplerate=tasa_muestreo, channels=1)
sd.wait()

# Obtener la señal capturada
señal_capturada = captura_audio.flatten()

# Sincronización de la señal de entrada
inicio_sincronizacion = 0
for i in range(len(señal_capturada) - 1):
    if señal_capturada[i] < 0 and señal_capturada[i + 1] >= 0:
        inicio_sincronizacion = i
        break

# Recuperación de la señal modulada
tiempo_símbolo = duración_símbolo
señal_recuperada = []
muestra_actual = inicio_sincronizacion
while muestra_actual + int(tiempo_símbolo * tasa_muestreo) < len(señal_capturada):
    muestra = señal_capturada[muestra_actual:muestra_actual + int(tiempo_símbolo * tasa_muestreo)]
    fase_promedio = np.angle(np.mean(muestra * np.exp(-1j * 2 * np.pi * frecuencia_portadora * np.arange(len(muestra)) / tasa_muestreo)))
    símbolo_recuperado = 0 if fase_promedio < np.pi else 1
    señal_recuperada.append(símbolo_recuperado)
    muestra_actual += int(tiempo_símbolo * tasa_muestreo)

# Convertir los símbolos recuperados a una cadena de bits
cadena_bits_recuperada = ''.join(str(bit) for bit in señal_recuperada)

# Mostrar la cadena de bits recuperada
print("Cadena de bits recuperada:", cadena_bits_recuperada)
