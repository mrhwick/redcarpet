
from audio import Audio
import os
from facepp import File, API


SERVER = 'http://api.us.faceplusplus.com/'

API_KEY = '83512035a89abd3721230e94caea54c4'
API_SECRET = 'Mv2y5KogIgHyvtv9vj2fn9BawJCNkj_-'

class Recognize(object):

    def __init__(self):
        self.audio = Audio()
        self.people={
            'Anthony Blardo': 'downfall.wav',
            'Matt Hardwick': 'fall.wav',
            'Daniel Hawkins': 'media.wav',
            'Allan Davis': 'vader.wav',
            'Tiffanie Robinson': 'girl.wav',
        }

    def is_person(self, image_file):
        path = 'media/image/face.png'
        # path = os.path.join('media/image/', image_file.filename)
        image_file.save(path)

        # import ipdb; ipdb.set_trace()
        f = File(path)
        api = API(API_KEY, API_SECRET, SERVER)

        print("Sending face to api")

        response = api.recognition.identify(group_name='Hackathoners', img=f)

        print(response)

        faces = response['face']
        if len(faces) > 0:
            face = faces[0]
            name = face['candidate'][0]['person_name']

            if name in self.people.keys():
                print("Found " + name)
                self.audio.add_to_playlist(self.people[name])
                self.audio.play()
            else:
                self.audio.add_to_playlist('run.wav')
                self.audio.play()
                print("Did not match a person.")
