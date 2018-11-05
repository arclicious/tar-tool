# tar-tool (snapshot branch)
Lightweight terminal tar archive extractor written in Python. 
**The snapshot branch is unstable and is possibly full of bugs, so I recommend using it only for testing upcoming versions of tar-tool.**
# Requirements:

* Python 2 or newer.
* The latest version of the Tar package to be installed on target Linux box.
* The figlet package to be installed.

# Installation guide

1. Make sure that you have the latest version of the Tar package installed by typing:

           sudo apt-get update

   into Terminal.

2. Make sure that you've also got **Python 2** or newer installed by typing:

          sudo apt-get install python2
          
   into Terminal.

3. Also, make sure that you've got figlet installed by typing:

          sudo apt-get install figlet


   into Terminal.


3. Clone the repository by typing:
         
         git clone https://github.com/arclicious/tar-tool.git

   into Terminal.
   
4. Open the downloaded folder with your file manager of choice.


5. Copy the tar.py file located in the cloned repository folder to the folder where all of your downloads are stored (eg. /home/USERNAME/Downloads)


6. You're all set!

# Running tar-tool

You can quickly and easily run tar-tool by cd-ing into your download directory (which tar.py is located in) and then typing:

          python3 tar.py

into Terminal.

Choose one of the choices that are shown to you when tar-tool is ran, and you're done!

**Repeat this process every time you download .tar archives you want to install.
