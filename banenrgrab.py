# Author  - Hades.y2k
# Date    - 01/06/2015
# License - <GPL v2>

import socket

class bcolors:
    RED = '\033[91m'
    BOLD = '\033[1m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    WARNING = '\033[93m'


class BGrab():
    print
    print bcolors.RED + " #====" + bcolors.ENDC + bcolors.BOLD + "   SIMPLE BANNER GRABBING   " + bcolors.ENDC + bcolors.RED + "=============#" + bcolors.ENDC
    print bcolors.RED + " #===================" + bcolors.ENDC + bcolors.BOLD + "   02/06/2015   " + bcolors.ENDC + bcolors.RED + "==========#" + bcolors.ENDC
    print bcolors.RED + " #=======================" + bcolors.ENDC + bcolors.BOLD + "   Hades.y2k   " + bcolors.ENDC + bcolors.RED + "=======#" + bcolors.ENDC
    print

    def __init__(self):
        self.engage()

        
    def Banner(self, ip, port):
        try:
            socket.setdefaulttimeout(5)
            soc = socket.socket()
            soc.connect((ip, port))
            banner = soc.recv(1024)
            return banner
        except:
            return

    def engage(self):
        # Initialize
        portlist = [21,22,25,80,110,443]
        host = raw_input("Enter the host name: ")
        print bcolors.WARNING + '[+]' + bcolors.ENDC + bcolors.BOLD + " Engaging the Target" + bcolors.ENDC + "\n"
        init_ip = socket.gethostbyname(host)

        # This first-3 of ip method comes from pingsweep.py from the-c0d3r pynmap.
        octets = init_ip.split('.')
        # got 4 octets now
        # get first 3 octets, combine them with '.'
        # and iterate from 0 to 255 for the last octet
        ip = str(octets[0]+"."+octets[1]+"."+octets[2]+".")

        for i in range(0,256):
            for port in portlist:
                ip_address = ip + str(i)
                banner = self.Banner(ip_address, port)
                if banner:
                    print bcolors.OKGREEN + "[+] " + bcolors.ENDC + bcolors.BOLD + ip_address + bcolors.ENDC + ':' + bcolors.BOLD + banner + bcolors.ENDC

if __name__ == '__main__':
    BGrab()
