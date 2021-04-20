#setting up selenium using pip3 and installing google chrome 
sudo apt install unzip python3-pip nautilus
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
echo 'extract the driver using unzip and past it to any path location /bin(recommended)'
echo 'you may need root privilege to paste files into /bin use the command "sudo nautilus" to open nautilus in root mode to paste directly'
read -p 'Press enter to continue'
echo 'done'
python3 req.py
