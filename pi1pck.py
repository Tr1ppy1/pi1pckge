#!/bin/bash

# Update package lists
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove

# Install essential packages
sudo apt install -y python3-pip python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev

# Upgrade pip
sudo pip3 install --upgrade pip

# Install Pi-hole dependencies
sudo pip3 install dnspython

# Install additional libraries for general programming
sudo pip3 install numpy pandas matplotlib

# Install Pi-hole
curl -sSL https://install.pi-hole.net | bash

# Note: The above command will prompt for some configuration options. Make sure to follow the instructions.

# Optional: Install additional Python libraries as per your requirements

echo "Installation completed!"
