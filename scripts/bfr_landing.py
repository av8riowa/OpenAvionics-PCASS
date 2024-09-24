import os
from pygame import mixer

AUDIO_DIR = '/home/pi/PCASS/audio/'

def play_bfr_landing():
    mixer.init()
    mixer.music.load(os.path.join(AUDIO_DIR, 'BfrLand.mp3'))
    mixer.music.play()

if __name__ == "__main__":
    play_bfr_landing()

