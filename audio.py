
import os
import pyaudio
from pydub import AudioSegment
from threading import Thread
import wave


class Audio(object):

    def __init__(self):
        self.block = 4
        self.thread = Thread(target=self.do_playback)
        self.playlist = []

    @property
    def is_playing(self):
        return self.thread.is_alive()

    def play(self):
        if not self.is_playing:
            self.thread = Thread(target=self.do_playback)
            self.thread.start()

    def do_playback(self):

        while len(self.playlist) > 0:

            wf = wave.open('media/wav/' + self.playlist.pop(), 'rb')

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

    def add_to_playlist(self, filename):
        self.playlist.insert(0, filename)

    def convert_mp3_to_wav(self, mp3_filename):

        # Get the mp3 data.

        sound_file = AudioSegment.from_mp3('media/mp3/' + mp3_filename)

        # Slice the file extension.

        filename_less_extension = os.path.splitext(mp3_filename)[0]

        # Give it a wav extension.

        wav_filename = filename_less_extension + '.wav'

        # Export the wav version for playback.

        sound_file.export('media/wav/' + wav_filename, format='wav')
