# -*- coding: utf-8 -*-

import time
import os
import subprocess
import socket

try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip3 not installed')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('[!] pip3 installed succesfully')

try:
    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')

try:
    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')

os.system("clear")

def get_local_ip():
    # Create a UDP socket to find the local IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to any IP address on port 1
        s.connect(('8.8.8.8', 1))
        local_ip = s.getsockname()[0]
    except Exception as e:
        print("Error getting local IP address:", e)
        local_ip = None
    finally:
        s.close()
    return local_ip

def ma_ip():
    url = 'https://www.myexternalip.com/raw'
    local_ip = get_local_ip()
    get_ip = requests.get(url, proxies=dict(http=f'http://{local_ip}:9050', https=f'http://{local_ip}:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print('[+] Your IP has been Changed to : ' + str(ma_ip()))

print('''\033[1;32;40m \n
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                V 2.1
from mrFD
''')
print("\033[1;40;31m http://facebook.com/ninja.hackerz.kurdish/\n")

# os.system("service tor start")  # Comment this line out if you are not using TOR

time.sleep(3)
print("\033[1;32;40m change your SOCKES to 127.0.0.1:9050 \n")
# os.system("service tor start")  # Comment this line out if you are not using TOR

x = input("[+] time to change Ip in Sec [type=60] >> ")
lin = input("[+] how many time do you want to change your ip [type=1000] for infinite ip change type [0] >> ")

if int(lin) == int(0):
    while True:
        try:
            time.sleep(int(x))
            change()
        except KeyboardInterrupt:
            print('\nauto tor is closed ')
            quit()
else:
    for i in range(int(lin)):
        time.sleep(int(x))
        change()
