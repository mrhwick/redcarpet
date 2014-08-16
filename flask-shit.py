from flask import Flask
app = Flask('walkout')

from audio import Audio

@app.route("/")
def hello():
    print('hello')
    a = Audio()
    a.convert_mp3_to_wav('run.mp3')
    a.play('sound.wav')
    return 'yo'

if __name__ == "__main__":
  app.run()