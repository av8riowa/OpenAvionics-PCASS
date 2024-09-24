from pygame import mixer

def stop_audio():
    mixer.init()
    mixer.music.stop()

if __name__ == "__main__":
    stop_audio()

