#!/bin/bash

# Install dependencies for touchscreen
sudo apt update
sudo apt install -y xserver-xorg xinit xserver-xorg-video-fbdev

# Download the appropriate drivers for the WaveShare 3.5-inch touchscreen
git clone https://github.com/waveshare/LCD-show.git
cd LCD-show/

# Set up the 3.5-inch screen driver
sudo ./LCD35-show

# After installation, reboot the system
sudo reboot

