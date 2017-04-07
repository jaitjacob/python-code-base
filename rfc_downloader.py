#Program : A tool for downloading Requesting for Comments (RFC) documents #from IETF, and then display them on screen.
#Date : 07/04/2017

import sys,urllib.request

try:
    rfc_number=int(sys.argv[1])
except(IndexError, ValueError):  #incase you don't pass a RFC number or you #pass an invalid RFC number this error is called upon
 print('RFC number not supplied')
 sys.exit(2)

template='http://www.ietf.org/rfc/rfc{}.txt'
url = template.format(rfc_number)

rfc_raw=urllib.request.urlopen(url).read()
rfc=rfc_raw.decode()

print(rfc)
