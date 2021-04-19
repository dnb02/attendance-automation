#setting up selenium using pip3 and installing google chrome 
sudo apt install unzip
pip3 install selenium
sudo apt update
CURR=$(pwd)
USER=$(whoami)
cd /home/$USER/Downloads
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
cd $CURR
google-chrome --version
echo 'Please find and install the suitable version webdriver for selenium'
echo 'https://chromedriver.chromium.org/getting-started'
read -p 'Press enter to continue'
echo 'done'
python3 req.py
