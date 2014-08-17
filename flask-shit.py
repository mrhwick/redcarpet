from flask import Flask
from flask import request

app = Flask('walkout')


from audio import Audio
from recognition import Recognize

a = Audio()

playlist = (
    'run.mp3',
    'media.mp3',
    'fall.mp3',
    'downfall.mp3',
    'vader.mp3',
    'girl.mp3',
)

for mp3 in playlist:
    a.convert_mp3_to_wav(mp3)

recog = Recognize()

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/face", methods=['POST'])
def face_dump():
    print("Getting file from request.")
    file = request.files['file']
    if file and allowed_file(file.filename):
        print("Checking for face.")
        recog.is_person(file)
    return ''


@app.route("/theme/<name>")
def play_input(filename):
    print('playing ' + filename)

    if a.is_playing:
        print('adding to playlist.')

    a.add_to_playlist(filename)
    a.play()
    return 'playing ' + filename

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)