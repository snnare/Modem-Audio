import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo de audio
filename = "C:\Proyects\Modem-Audio\FSK.wav"
sample_rate, audio = wav.read(filename)

# Obtener los valores de amplitud del audio
# audio = audio[:, 0]  # Si el audio es estéreo, considera solo un canal (izquierdo o derecho)

# Crear el eje de tiempo en segundos
time = np.arange(0, len(audio)) / sample_rate

# Graficar el audio
plt.figure(figsize=(10, 4))
plt.plot(time, audio)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Gráfico de audio")
plt.show()
