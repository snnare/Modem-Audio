import sounddevice as sd
import numpy as np
import soundfile as sf

# FSK
fs = 44100  # Frecuencia de muestreo en Hz
duracion_tono = 0.2  # Duración del tono en segundos
f0 = 1000  # Frecuencia de la señal portadora para el bit 0
f1 = 2000  # Frecuencia de la señal portadora para el bit 1


def files_to_binary_representation(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    # Convert binary data to a string of binary digits
    binary_string = ''.join(format(byte, '08b') for byte in binary_data)
    return binary_string

def modular_bit(bit):
    if bit == 0:
        frecuencia_portadora = f0
    else:
        frecuencia_portadora = f1
    
    tiempo = np.linspace(0, duracion_tono, int(fs * duracion_tono), endpoint=False)
    signal_portadora = np.sin(2 * np.pi * frecuencia_portadora * tiempo)
    
    return signal_portadora

 
def modular_cadena(cadena):
    signal_modulada = np.array([], dtype=np.float32)
    
    for caracter in cadena:
        bits = np.unpackbits(np.array([ord(caracter)], dtype=np.uint8))
        print(bits)
        for bit in bits:
            signal_modulada = np.concatenate((signal_modulada, modular_bit(bit)))
       
    return signal_modulada


mensaje = "Hola como estas hoy"
signal_modulada = modular_cadena(mensaje)

sd.play(signal_modulada, fs)
sf.write('FSK.wav', signal_modulada, fs)
sd.wait()
