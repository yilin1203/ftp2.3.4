import socket
import sys
import os
from threading import Thread
from optparse import OptionParser

def getBanner(ip,port):
    socket.setdefaulttimeout(2)
    s = socket.socket()
    try:
        s.connect((ip,port))
        banner = s.recv(1024)
        s.close()
        return banner
    except:
        return

def chekVulns(ip,port):
    banner = getBanner(ip,port)
    if banner:
        if banner == b'220 (vsFTPd 2.3.4)\r\n':
            print(ip,"is vulnerable")
        else:
            print(ip,"is unvulnerable")
    else:
        print(ip,"not get banner")

def main():
    show = r'''
     __      _______ ______ _______ _____ ___    ____  _  _   
     \ \    / / ____|  ____|__   __|  __ \__ \  |___ \| || |  
      \ \  / / (___ | |__     | |  | |__) | ) |   __) | || |_ 
       \ \/ / \___ \|  __|    | |  |  ___/ / /   |__ <|__   _|
        \  /  ____) | |       | |  | |    / /_ _ ___) |  | |  
         \/  |_____/|_|       |_|  |_|   |____(_)____(_) |_| 

                                                    by：
    '''
    print(show + '\n')

    usage = "%prog [-h] [-i ip] [-f ip.txt]"
    parser = OptionParser(usage=usage)
    parser.add_option("-f", "--file", type="string", dest="filename", help="specify trrhe IP address file")
    parser.add_option("-i", "--ip", type="string", dest="address", help="specify the address")
    (options, args) = parser.parse_args()

    filename = options.filename
    address = options.address

    if filename == None and address == None:
        print("请指定IP列表文件或者IP地址")
        sys.exit()

    if filename:
        if not os.path.exists(filename):
            print("指定的文件不存在，请重新输入")
            sys.exit()
        f = open(filename,"r")
        for i in f.readlines():
            ip = i.strip("\n")
            port = 21
            t = Thread(target = chekVulns,args = (ip,port))
            t.start()
        f.close()

    if address:
        ip = address
        port = 21
        t = Thread(target=chekVulns, args=(ip, port))
        t.start()

if __name__ == "__main__":
    main()