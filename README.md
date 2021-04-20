# Pong-application-using-kivy

# Requirement.txt
- Open terminal and run "python3 -m pip install -r requirement.txt"

# Python to Andriod APK
- <b> Downloading dependencies </b>
- "sudo apt-get install python3-distutils"
- "sudo apt-get install libltdl-dev libffi-dev libssl-dev autoconf autotools-dev"
- "sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev"
- "pip3 install --user --upgrade Cython==0.29.19" (If created virtual env then remove --user)
- "export PATH=$PATH:~/.local/bin/"
- <hr>
- <b>Cloning buildozer</b>
- "git clone https://github.com/kivy/buildozer.git"
- <hr>
- <b>Setup of buildozer</b>
- "cd buildozer/"
- "sudo python3 setup.py install"
- "cd .." (Come back where your kivy main.py file is located)
- "buildozer init"
- "buildozer android debug" 
- Now this will take more than 40 minutes for first time depending on internet speed and machine specs
- and after that your Andriod APK file will be in /bin folder and that's it now you can develop apps with python.
