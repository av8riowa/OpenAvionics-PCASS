import os
from pygame import mixer

AUDIO_DIR = '/home/pi/PCASS/audio/'

def play_seatbelt_sign():
    mixer.init()
    mixer.music.load(os.path.join(AUDIO_DIR, 'SBsign.mp3'))
    mixer.music.play()

if __name__ == "__main__":
    play_seatbelt_sign()

