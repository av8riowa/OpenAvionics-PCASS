import os
from pygame import mixer

AUDIO_DIR = '/home/pi/PCASS/audio/'

def play_pax_briefing():
    mixer.init()
    mixer.music.load(os.path.join(AUDIO_DIR, 'PaxBrief.mp3'))
    mixer.music.play()

if __name__ == "__main__":
    play_pax_briefing()

