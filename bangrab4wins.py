# Author  - Hades.y2k
# Date    - 04/06/2015
# Version - 2.0
# License - <GPL v2>

import socket
import thread
from sys import platform

# Initialize
portlist = [21,22,25,80,110,443] # You can add more.

class BGrab():
    print "\n #====   SIMPLE BANNER GRABBING   =============#"
    print " #==================  v2 04/06/2015   =========#"
    print " #=======================   Hades.y2k   =======#\n"


    def __init__(self):
        self.enumerate()

    def first(self,ip):
        for x in range(0,129):
            for port in portlist:
                ip_address = ip + str(x)
                banner = self.Banner(ip_address, port)
                if banner:
                    print "[+] " + ip_address + ':' + banner

    def second(self,ip):
        for x in range(129,256):
            for port in portlist:
                ip_address = ip + str(x)
                banner = self.Banner(ip_address, port)
                if banner:
                    print "[+] " + ip_address + ':' + banner

    def Banner(self, ip, port):
        try:
            socket.setdefaulttimeout(2)
            soc = socket.socket()
            soc.connect((ip, port))
            banner = soc.recv(1024)
            return banner
        except:
            return

    def enumerate(self):
        # Initialize
        host = raw_input("Enter the host name: ")
        print "[+] Engaging the Target\n"
        init_ip = socket.gethostbyname(host)

        # This first-3 of ip method comes from pingsweep.py from the-c0d3r pynmap.
        octets = init_ip.split('.')
        # got 4 octets now
        # get first 3 octets, combine them with '.'
        # and iterate from 0 to 255 for the last octet
        ip = str(octets[0]+"."+octets[1]+"."+octets[2]+".")

        thread.start_new_thread(self.first(ip), ())
        thread.start_new_thread(self.second(ip), ())


if __name__ == '__main__':
    if 'linux' in platform:
        print "[!] Sorry, This script is only for Windows users."
        print "    There's one for Linux users. Check the Below Link."
        print "    www.github.com/Hadesy2k/banner-grab\n"
    else:
        BGrab()
