import os
import tkinter as tk
from pygame import mixer

# Initialize the audio mixer
mixer.init()

# Path to audio files
AUDIO_DIR = '/home/pi/PCASS/audio/'

# Function to play audio files
def play_audio(file):
    mixer.music.load(os.path.join(AUDIO_DIR, file))
    mixer.music.play()

# Function to stop audio
def stop_audio():
    mixer.music.stop()

# GUI Setup
root = tk.Tk()
root.title("PCASS")

# Set the window size to match the 320x480 touchscreen
root.geometry("320x480")

# Create seatbelt sign button
def seatbelt_sign_toggle():
    # Play seatbelt sign audio and toggle text on button
    play_audio('SBsign.mp3')
    seatbelt_btn.config(text="Seatbelt ON" if seatbelt_btn.cget("text") == "Seatbelt OFF" else "Seatbelt OFF")

seatbelt_btn = tk.Button(root, text="Seatbelt OFF", command=seatbelt_sign_toggle, height=2, width=25)
seatbelt_btn.pack(pady=10)

# Create cabin alert button
cabin_alert_btn = tk.Button(root, text="Cabin Alert", command=lambda: play_audio('CabinAlert.mp3'), height=2, width=25)
cabin_alert_btn.pack(pady=10)

# Create boarding music button
boarding_music_btn = tk.Button(root, text="Boarding Music", command=lambda: play_audio('BoardingMusic.mp3'), height=2, width=25)
boarding_music_btn.pack(pady=10)

# Create passenger briefing button
pax_briefing_btn = tk.Button(root, text="Passenger Briefing", command=lambda: play_audio('PaxBrief.mp3'), height=2, width=25)
pax_briefing_btn.pack(pady=10)

# Create before landing briefing button
bfr_landing_btn = tk.Button(root, text="Before Landing Briefing", command=lambda: play_audio('BfrLand.mp3'), height=2, width=25)
bfr_landing_btn.pack(pady=10)

# Create stop button
stop_btn = tk.Button(root, text="STOP", command=stop_audio, height=2, width=25)
stop_btn.pack(pady=10)

# Main loop
root.mainloop()
