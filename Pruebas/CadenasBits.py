import sounddevice as sd
import numpy as np
import soundfile as sf

# FSK
fs = 44100  # Frecuencia de muestreo en Hz
duracion_tono = 0.1  # Duración del tono en segundos
f0 = 1000  # Frecuencia de la señal portadora para el bit 0
f1 = 2000  # Frecuencia de la señal portadora para el bit 1

def modular_bits(bit):
    if bit == 0:
        frecuencia_portadora = f0
    else:
        frecuencia_portadora = f1
    
    tiempo = np.linspace(0, duracion_tono, int(fs * duracion_tono), endpoint=False)
    sin_port = np.sin(2 * np.pi * frecuencia_portadora * tiempo)
    
    return sin_port

def cad_a_bin(cadena0):
    result = ''.join(format(ord(c), 'b') for c in cadena0)
    return result


mensaje = "Hola como estas compadrito"
cadena_bits = cad_a_bin(mensaje)
print(cadena_bits)
senial_final = modular_bits(cadena_bits)

sd.play(senial_final, fs)
sf.write('Apoco_si.wav', senial_final, fs)
sd.wait()