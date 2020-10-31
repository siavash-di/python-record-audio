import pyaudio
import wave

# Start
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, input=True, frames_per_buffer=1024)

frames = []
for i in range(0, int(44100 / 1024 * 5)):
    data = stream.read(1024)
    frames.append(data)

# Stop
stream.stop_stream()
stream.close()
p.terminate()

# Write file
wf = wave.open("test.wav, 'wb')
wf.setnchannels(2)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wf.setframerate(44100)
wf.writeframes(b''.join(frames))
wf.close()
