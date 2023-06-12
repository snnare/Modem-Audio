import sounddevice as sd
import soundfile as sf

fs = 44100  # Frecuencia de muestreo en Hz
duration = 10  # Duración de la grabación en segundos

# Grabar audio desde el puerto de 3.5 mm
print("Grabando audio desde el puerto de 3.5 mm...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

# Guardar la grabación en un archivo WAV
file_name = "grabacion.wav"
sf.write(file_name, recording, fs)

print(f"La grabación se guardó en {file_name}.")
#hola