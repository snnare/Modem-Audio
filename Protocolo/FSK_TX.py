import sounddevice as sd
import numpy as np
import soundfile as sf

# FSK
fs = 44100  # Frecuencia de muestreo en Hz
duracion_tono = 0.1  # Duración del tono en segundos
f0 = 1000  # Frecuencia de la señal portadora para el bit 0
f1 = 2000  # Frecuencia de la señal portadora para el bit 1

# 0011011
def modular_bit(bit):
    if bit == 0:
        frecuencia_portadora = f0
    else:
        frecuencia_portadora = f1
    
    tiempo = np.linspace(0, duracion_tono, int(fs * duracion_tono), endpoint=False)
    señal_portadora = np.sin(2 * np.pi * frecuencia_portadora * tiempo)
    
    return señal_portadora

 
def modular_cadena(cadena):
    señal_modulada = np.array([], dtype=np.float32)
    
    for caracter in cadena:
        bits = np.unpackbits(np.array([ord(caracter)], dtype=np.uint8))
        
        for bit in bits:
            señal_modulada = np.concatenate((señal_modulada, modular_bit(bit)))
       
    return señal_modulada


mensaje = "Adios"
señal_modulada = modular_cadena(mensaje)
señal = modular_bit()


print(señal_modulada)

#sd.play(señal_modulada, fs)
#sf.write('FSK.wav', señal_modulada, fs)
#sd.wait()
