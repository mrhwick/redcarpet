
import pyaudio
from pydub import AudioSegment
import wave


class Audio(object):

    def __init__(self):
        self.block = 4

    def play(self, filename):
        wf = wave.open(filename, 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(self.block)

        while data != '':
            stream.write(data)
            data = wf.readframes(self.block)

        stream.stop_stream()
        stream.close()

        p.terminate()

    def convert_mp3_to_wav(self, mp3_filename):
        sound_file = AudioSegment.from_mp3(mp3_filename)
        sound_file.export('sound.wav', format='wav')
