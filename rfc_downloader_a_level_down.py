#This python code shows the same implementation of the rfc downloader assuming HTTP was brand new and there was
#no module (the "urllib" module,i meant) in Python that could do the magic for us.
#Here, we step down one step in the protocol stack and use TCP to to download the required RFC document.

#The Internet is like a cake with many layers, now these layers we're talking about is an analogy to the Internet protocol suite that works
#with each other to get packets delivered from one place to another.

#Python provides modules to interface with different protocols.

import sys,socket    #we had imported a different module in the previous program and that handled all the HTTP header for us.

try:
    rfc_number=int(sys.argv[1])
except (IndexError, ValueError):
    print('Please supply an RFC number as an argument.')
    sys.exit(2)
    
 host = 'www.ietf.org'
 port = 80
 socket = socket.create_connection((host,port))
 
 req = (
     'GET /rfc/rfc{rfcnum}.txt HTTP/1.1\r\n'
     'Host: {host}:{port}\r\n'
     'User-Agent: Python {version}\r\n'
     'Connection: close\r\n'
     '\r\n'
 )
 
 req=req.format(
     rfcnum=rfc_number,
     host=host,
     port=port,
     version=sys.version_info[0]
)

socket.sendall(req.encode('ascii'))
rfc_raw = bytearray()
while True:
    buf = sock.recv(4096)
    if not len(buf):
        break
    rfc_raw += buf
rfc = rfc_raw.decode('utf-8')
print(rfc)

