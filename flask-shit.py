from flask import Flask
from flask import request
app = Flask('walkout')

from audio import Audio

a = Audio()
a.convert_mp3_to_wav('run.mp3')

@app.route("/face", methods=['POST'])
def face_dump():

    return ''


@app.route("/play/<filename>")
def play_input(filename):
    print('playing ' + filename)

    if a.is_playing:
        print('adding to playlist.')

    a.add_to_playlist(filename)
    a.play()
    return 'playing ' + filename

if __name__ == "__main__":
  app.run(host='0.0.0.0')