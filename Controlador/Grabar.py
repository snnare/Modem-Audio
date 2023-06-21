import soundfile as sf
import numpy as np
import pyaudio
import wave

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

def grabar(duracion, ruta):
    # Configuración de la grabación
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
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

grabar(8, 'Sonidos\Diana.wav')
data, samplerate = sf.read('Sonidos\Diana.wav')

