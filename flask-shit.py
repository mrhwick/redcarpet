from flask import Flask
from flask import request

app = Flask('walkout')


from audio import Audio
import os

a = Audio()
a.convert_mp3_to_wav('run.mp3')

app.config['UPLOAD_FOLDER'] = 'media/image/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/face", methods=['POST'])
def face_dump():
    file = request.files['file']
    if file and allowed_file(file.filename):
        # import ipdb; ipdb.set_trace()
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
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