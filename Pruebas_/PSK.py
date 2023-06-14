import numpy as np
import sounddevice as sd

# Parámetros de la modulación PSK
frecuencia_portadora = 4000  # Frecuencia de la portadora en Hz
tasa_muestreo = 44100  # Tasa de muestreo en muestras por segundo
bits_por_simbolo = 1  # Número de bits por símbolo (PSK binaria)
duración_símbolo = 0.1  # Duración de cada símbolo en segundos

# Cadena de bits a modular (ejemplo)
cadena_bits = "010101010101"

# Mapeo de bits a símbolos (0 -> 0 grados, 1 -> 180 grados)
símbolos = [0 if bit == '0' else 180 for bit in cadena_bits]

# Generación de la señal modulada
tiempo_símbolo = duración_símbolo
tiempo_total = len(símbolos) * tiempo_símbolo
tiempo = np.linspace(0, tiempo_total, int(tiempo_total * tasa_muestreo), endpoint=False)
señal_modulada = np.zeros_like(tiempo)

for i, símbolo in enumerate(símbolos):
    fase = np.radians(símbolo)
    señal_modulada[i * int(tiempo_símbolo * tasa_muestreo):(i + 1) * int(tiempo_símbolo * tasa_muestreo)] = np.cos(2 * np.pi * frecuencia_portadora * tiempo[i * int(tiempo_símbolo * tasa_muestreo):(i + 1) * int(tiempo_símbolo * tasa_muestreo)] + fase)

# Normalizar la señal para evitar distorsiones
señal_modulada /= np.max(np.abs(señal_modulada))

# Reproducir la señal como audio
sd.play(señal_modulada, tasa_muestreo)
sd.wait()
