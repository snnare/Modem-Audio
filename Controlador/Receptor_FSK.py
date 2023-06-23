import pyaudio
import wave

class Grabadora:
    def __init__(self, duracion, ruta, fs):
        self.duracion = duracion
        self.ruta = ruta
        self.fs = fs
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.CHUNK = 1024

    def grabar(self):
        # Configuración de la grabación
        RECORD_SECONDS = self.duracion
        WAVE_OUTPUT_FILENAME = self.ruta

        # Inicializar Pyaudio
        audio = pyaudio.PyAudio()

        # Abrir el microfono
        stream = audio.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.fs,
            input=True,
            frames_per_buffer=self.CHUNK
        )

        print('Grabando...')

        frames = []
        for i in range(0, int(self.fs / self.CHUNK * RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        print('¡Finalizó!')

        # Detener y cerrar el stream de audio
        stream.stop_stream()
        stream.close()
        audio.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(audio.get_sample_size(self.FORMAT))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(frames))
        wf.close()
