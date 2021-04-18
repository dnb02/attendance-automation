#setting up selenium using pip3 and installing google chrome 

pip3 install selenium
sudo apt update
CURR=$(pwd)
USER=$(whoami)
cd /home/$USER/Downloads
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
cd $CURR
