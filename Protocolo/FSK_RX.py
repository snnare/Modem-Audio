import soundfile as sf
import numpy as np

fs = 44100  # Frecuencia de muestreo en Hz
duracion_tono = 0.1  # Duración del tono en segundos
f0 = 1000  # Frecuencia de la señal portadora para el bit 0
f1 = 2000  # Frecuencia de la señal portadora para el bit 1

def demodular_bit(señal_portadora):
    espectro = np.fft.fft(señal_portadora)
    
   # Identificar los índices de las frecuencias portadoras
    indice_f0 = int(f0 * duracion_tono * len(espectro) / fs)
    indice_f1 = int(f1 * duracion_tono * len(espectro) / fs)
    
    # Filtrar las componentes en el espectro correspondientes a las frecuencias portadoras
    componente_f0 = espectro[indice_f0]
    componente_f1 = espectro[indice_f1]
        
    # Comparar las magnitudes de las componentes y demodular el bit
    if abs(componente_f0) > abs(componente_f1):
        return 0
    else:
        return 1

def demodular_cadena(señal_modulada):
    duracion_bit = int(fs * duracion_tono)
    bits_demodulados = []
        
    for i in range(0, len(señal_modulada), duracion_bit):
        muestra = señal_modulada[i:i+duracion_bit]
        bit_demodulado = demodular_bit(muestra)
        bits_demodulados.append(bit_demodulado)
        
    return bits_demodulados

# Cargar la señal modulada desde un archivo
señal_modulada, fs = sf.read('FSK.wav')

# Demodular la señal
bits_demodulados = demodular_cadena(señal_modulada)

# Convertir los bits demodulados a caracteres
cadena_demodulada = ''
for i in range(0, len(bits_demodulados), 8):
    byte = bits_demodulados[i:i+8]
    caracter = chr(int(''.join([str(bit) for bit in byte]), 2))
    cadena_demodulada += caracter

print("Cadena demodulada:", cadena_demodulada)
