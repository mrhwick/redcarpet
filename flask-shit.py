from flask import Flask
from flask import request

app = Flask('walkout')


from audio import Audio
from recognition import Recognize

a = Audio()
a.convert_mp3_to_wav('run.mp3')
a.convert_mp3_to_wav('media.mp3')

recog = Recognize()

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/face", methods=['POST'])
def face_dump():
    file = request.files['file']
    if file and allowed_file(file.filename):
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
  app.run(host='0.0.0.0')