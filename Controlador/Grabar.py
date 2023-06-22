import soundfile as sf
import numpy as np
import pyaudio
import wave
import scipy.fftpack as fourier
import matplotlib.pyplot as plt

def bfsk_modulate(bit_array, space_freq, mark_freq, baud, sample_rate):
    seconds_per_bit = 1 / baud
    samples_per_bit = int(sample_rate * seconds_per_bit)
    t = np.linspace(0, seconds_per_bit, samples_per_bit, endpoint=False)
    signal = np.array([])
    for bit in bit_array:
        if bit == 0:
            space = np.sin(2 * np.pi * space_freq * t)
            signal = np.append(signal, space)
        elif bit == 1:
            mark = np.sin(2 * np.pi * mark_freq * t)
            signal = np.append(signal, mark)
    return signal


def bfsk_demodulate_ffft(signal, space_freq, mark_freq, baud, sample_rate):
    gk =  fourier.fft(signal)
    M_gk = abs(gk)

    F = sample_rate*np.arange(0,len(signal))/len(signal)

    plt.plot(F, M_gk)
    plt.xlabel('Frecuencia (HZ)')
    plt.ylabel('Amplitud FFT')
    plt.show()

def bfsk_demodulate(signal, space_freq, mark_freq, baud, sample_rate):
    seconds_per_bit = 1 / baud
    samples_per_bit = int(sample_rate * seconds_per_bit)
    bit_array = np.array([])

    for i in range(0, len(signal), samples_per_bit):
        bit_samples = signal[i:i+samples_per_bit]
        correlation_space = np.correlate(bit_samples, np.sin(2 * np.pi * space_freq * np.linspace(0, seconds_per_bit, samples_per_bit, endpoint=False)))
        correlation_mark = np.correlate(bit_samples, np.sin(2 * np.pi * mark_freq * np.linspace(0, seconds_per_bit, samples_per_bit, endpoint=False)))

        if correlation_space > correlation_mark:
            bit_array = np.append(bit_array, 0)
        else:
            bit_array = np.append(bit_array, 1)

    return bit_array.astype(int)

def grabar(duracion, ruta, fs):
    # Configuración de la grabación
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = fs
    CHUNK = 1024
    RECORD_SECONDS = duracion
    WAVE_OUTPUT_FILENAME = ruta
    
    # Inicializar Pyaudio
    audio = pyaudio.PyAudio()

    # Abrir el microfono
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    print('Grabando...')

    frames = []
    for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print('!Finalizo')

    # Detener y cerrar el stream de audio
    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# grabar(10, 'Sonidos\A04.wav',96000)
data, samplerate = sf.read('Sonidos\A01.wav')

#demodulada = bfsk_demodulate(data,1000,2000,2,44100)
#print(demodulada)

bfsk_demodulate_ffft(data,1000, 2000,1,44100)


'''
1 baudio
A01 [1,1,1,1,0,0,0,0,1,0] 1000, 2000,1,44100
A02 [1,0,1,0,1,1,0,0,1,0] 1000, 2000,1,44100
A03 [1,0,1,0,1,1,0,0,1,0] 1000, 4000,1,96000
    2 baudios
A04 [1,0,1,0,1,1,0,0,1,0] 400, 1000,2,96000 no sirve jajaja
A04 [1,0,1,0,1,1,0,0,1,0] 400, 1000,2,96000
'''