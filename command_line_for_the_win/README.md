# Command line for the win Project
## Steps to use sftp:
### connecting to the server
first you need to establish a connection between your local host
and the server and its quiet easy

$ sftp <host-address>
$ sftp exmaple.alx-cod.online

than the server will ask you to enter the password

### navigation through server
navigation through the server is also easy because you will use the same way you use with your local host

sftp> cd <desired-path>

### transfer files to the server
and the last thing is to transfer the files to your server and it also easy 
you simply use "put" command with file name

sftp> put <file-name>
sftp> put image.png
