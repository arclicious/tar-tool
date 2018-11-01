# Written by u/arclicious on Reddit to make extracting tar archives much more easier!
import os
import sys
os.system("clear")
print("[!] To use this application you must have tar installed.")
print("[!] tar-tool will only work with Python 3.6 or newer.")
try:
    os.system("figlet -c -f slant Tar Tool")
except:
    sys.exit()
print("Menu:")
print("")
print("1. Extract a tar.gz file")
print("2. Extract a tar.bz2 file")
print("3. Extract a tar.xz file")
print("")
inp = input("What would you like to do?")
if inp == "1":
    inp = input("1. What is the name of the file that you would like to extract (without .tar.gz extension)?")
    print("[*] Extracting file...")
    os.system("tar -xzvf %s" % inp + ".tar.gz")
    print("[*] Extracted file!")
    sys.exit()
elif inp == "2":
    inp = input("1. What is the name of the file that you would like to extract (without .tar.bz2 extension)?")
    print("[*] Extracting file...")
    os.system("tar -jvf %s" % inp + ".tar.bz2")
    print("[*] Extracted file!")
    sys.exit()
elif inp == "3":
    inp = input("1. What is the name of the file that you would like to extract (without .tar.xz extension)?")
    print("[*] Extracting file...")
    os.system("tar -xJvf %s" % inp + ".tar.xz")
    print("[*] Extracted file!")
    sys.exit()
else:
    sys.exit()
