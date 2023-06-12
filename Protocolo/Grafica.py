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

# Graficar el audio en el dominio del tiempo
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.plot(time, audio)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Gráfico de audio")

# Calcular la transformada de Fourier
fft = np.fft.fft(audio)
freq = np.fft.fftfreq(len(audio), d=1/sample_rate)

# Graficar el espectro de frecuencia
plt.subplot(122)
plt.plot(freq, np.abs(fft))
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.title("Espectro de frecuencia")

plt.tight_layout()
plt.show()
