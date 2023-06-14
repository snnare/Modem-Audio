import soundfile as sf
import numpy as np

fs = 18000  # Sampling frequency in Hz
tone_duration = 0.2  # Duration of each tone in seconds
f0 = 1000  # Carrier frequency for bit 0
f1 = 2000  # Carrier frequency for bit 1

def demodulate_signal(signal, fs):
    bits_demodulated = []

    samples_per_tone = int(fs * tone_duration)

    for i in range(0, len(signal), samples_per_tone):
        tone = signal[i:i+samples_per_tone]

        frequency = np.fft.rfftfreq(len(tone), d=1.0/fs)
        spectrum = np.abs(np.fft.rfft(tone))

        index_f0 = np.argmax(spectrum[np.where(frequency == f0)])
        index_f1 = np.argmax(spectrum[np.where(frequency == f1)])

        bit_demodulated = 0 if index_f0 > index_f1 else 1
        bits_demodulated.append(bit_demodulated)

    return bits_demodulated


# Here, you would add code to receive the audio signal, for example, using sounddevice to record the signal.

# Once you have the recorded signal, you can demodulate it:
recorded_signal, _ = sf.read('FSK.wav')  # Read the recorded signal from the WAV file
bits_demodulated = demodulate_signal(recorded_signal, fs)

# Convert the demodulated bits to a text string
message_demodulated = ""
for i in range(0, len(bits_demodulated), 8):
    byte = bits_demodulated[i:i+8]
    character = chr(int(''.join(map(str, byte)), 2))
    message_demodulated += character

print("Demodulated message:", message_demodulated)