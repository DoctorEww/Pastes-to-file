import  urllib.request
import urllib.error
import re
#you need to set a path to a file to save these in for example...
#path="C:/Users/Lenny/Desktop/Python/passwords/"
path=""
#get the feed as html
resp=urllib.request.urlopen("http://feeds.feedburner.com/HaveIBeenPwnedLatestPastes").read()
print (resp)
#find the urls on the feed
urls = re.findall(r'<link>(.*?)</link>',str(resp))
for url in urls:
    #find the ones dealing with PasteBin
    if "http://pastebin.com" in url:
        #Add raw to the URL so you dont get that formating crap
        x=i[:20]+"raw/"+i[20:]
        #optional print statment
        print (x)
        try:
            #save the file as the name of the paste it is posible yet not likely that two will have the same name the first one will be overwritten
            z=urllib.request.urlopen(x).read()
            print(z)
            temp=i[20:]
            filez=open(path+temp+".txt","w")
            filez.write(str(z))
            filez.close()
        except Exception as e:
            print(i+" not found")
