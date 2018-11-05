# Written by u/arclicious on Reddit to make extracting tar archives much more easier!
import os
import sys
#debug = True - implementing at later date
os.system("clear")
already_done = 0
print("[!] To use tar-tool you must have tar and figlet installed.")
try:
    os.system("figlet -c -f slant Tar Tool 2.5-snapshotV1")
except:
    sys.exit()
def exit(msg):
	sys.exit(msg)

def main():
	try:
		print("Menu:")
		print("")
		print("1. Extract a tar.gz file")
		print("2. Extract a tar.bz2 file")
		print("3. Extract a tar.xz file")
		print("")
		inp = raw_input("What would you like to do?")
		if inp == "1":
			inp = raw_input("1. What is the name of the file that you would like to extract (without .tar.gz extension)?")
			print("[*] Extracting file...")			
			os.system("tar -xzvf %s" % inp + ".tar.gz")
			print("[*] Extracted file!")
			sys.exit()
		elif inp == "2":
			inp = raw_input("1. What is the name of the file that you would like to extract (without .tar.bz2 extension)?")
			print("[*] Extracting file...")
			print("tar -jvf %s" % inp + ".tar.bz2")
			os.system("tar jxf %s" % inp + ".tar.bz2")
			print("[*] Extracted file!")
			sys.exit()
		elif inp == "3":
			inp = raw_input("1. What is the name of the file that you would like to extract (without .tar.xz extension)?")
			print("[*] Extracting file...")
			os.system("tar -xJvf %s" % inp + ".tar.xz")
			print("[*] Extracted file!")
			sys.exit()
		else:
			sys.exit()
	except error as Exception:
		print(e)
	


try:
	if already_done == 0:
		raw_input("Please press return to continue.") # If 3.X python is being used, will cause error and move onto except
		print("Detected 2.X version of Python") # Will be removed in master branch.
		already_done = 1
		main() 
	else:
		sys.exit()
	
except:
	if already_done == 0:
		raw_input = input
		input("Please press return to continue.")
		print("Detected 3.X version of Python") # Will be removed in master branch.
		already_done = 1
		main()
	else:
		sys.exit()
