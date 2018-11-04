# Written by u/arclicious on Reddit to make extracting tar archives much more easier!
import os
import sys
debug = True
os.system("clear")
print("[!] To use tar-tool you must have tar and figlet installed.")
try:
    os.system("figlet -c -f slant Tar Tool 2.4")
except:
    sys.exit()

def p():
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
	raw_input("Please press [RETURN] in order to continue.")
	print("Detected 2.X version of Python")
	p()
except:
    raw_input = input
    input("Please press [RETURN] to continue.")
    print("Detected 3.X version of Python")
    p()
