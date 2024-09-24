import os
from pygame import mixer

AUDIO_DIR = '/home/pi/PCASS/audio/'

def play_cabin_alert():
    mixer.init()
    mixer.music.load(os.path.join(AUDIO_DIR, 'CabinAlert.mp3'))
    mixer.music.play()

if __name__ == "__main__":
    play_cabin_alert()

