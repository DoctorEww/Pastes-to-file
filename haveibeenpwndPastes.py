print ("hello world!")
import  urllib.request
import urllib.error
import re
url="http://feeds.feedburner.com/HaveIBeenPwnedLatestPastes"
resp=urllib.request.urlopen(url).read()
print (resp)
urls = re.findall(r'<link>(.*?)</link>',str(resp))
for i in urls:
    if "http://pastebin.com" in i:
        x=i[:20]+"raw/"+i[20:]
        print (x)
        try:
            z=urllib.request.urlopen(x).read()
            print(z)
            temp=i[20:]
            filez=open("C:/Users/Lenny/Desktop/Python/passwords/"+temp+".txt","w")
            filez.write(str(z))
            filez.close()
        except Exception as e:
            print(i+"not found")
