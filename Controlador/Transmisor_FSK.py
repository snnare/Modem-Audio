import numpy as np
import sounddevice as sd

class Codificador:
    def __init__(self):
        self.bit_array = []

    def encode_text(self, text):
        bit_array = []
        for char in text:
            binary = bin(ord(char))[2:].zfill(8)
            for bit in binary:
                bit_array.append(int(bit))
        self.bit_array = bit_array

    def get_bit_array(self):
        return self.bit_array


class BFSKModulator:
    def __init__(self, space_freq, mark_freq, baud, sample_rate):
        self.space_freq = space_freq
        self.mark_freq = mark_freq
        self.baud = baud
        self.sample_rate = sample_rate

    def modulate(self, bit_array):
        seconds_per_bit = 1 / self.baud
        samples_per_bit = int(self.sample_rate * seconds_per_bit)
        t = np.linspace(0, seconds_per_bit, samples_per_bit, endpoint=False)
        signal = np.array([])
        for bit in bit_array:
            if bit == 0:
                space = np.sin(2 * np.pi * self.space_freq * t)
                signal = np.append(signal, space)
            elif bit == 1:
                mark = np.sin(2 * np.pi * self.mark_freq * t)
                signal = np.append(signal, mark)
        return signal
    
class Transmitir:
    def __init__(self, space_freq, mark_freq, baud, sample_rate):
        self.codificador = Codificador()
        self.modulator = BFSKModulator(space_freq, mark_freq, baud, sample_rate)

    def transmit_text(self, text):
        self.codificador.encode_text(text)
        bit_array = self.codificador.get_bit_array()
        signal = self.modulator.modulate(bit_array)
        return signal

transmisor = Transmitir(space_freq=1000, mark_freq=2000, baud=4, sample_rate=44100)
texto = "Hola mundo!"
signal = transmisor.transmit_text(texto)
# print(signal)

sd.play(signal,44100)
sd.wait()