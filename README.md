# Web-Trojan
It is a python based trojan that can give you a reverse shell through wan without setting up port forwarding or ngrok . It has a trojan module and a handler . The handler writes the shell command to text file stored on a remote web-server . The trojan reads it and execute the command and writes the output to a text file which is read by the handler
