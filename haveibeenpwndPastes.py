import  urllib.request
import urllib.error
import re
#you need to set a path to a file to save these in, for example...
#path="/home/doctoreww/Desktop/Python/passwords/"
path=""
#get the feed as html
resp=urllib.request.urlopen("http://feeds.feedburner.com/HaveIBeenPwnedLatestPastes").read()
#find the urls on the feed
urls = re.findall(r'<link>(.*?)</link>',str(resp))
for url in urls:
    #find the ones dealing with PasteBin
    if "https://pastebin.com" in url:
        #print (url)# print the url you are doing (optional)
        #Add raw to the URL so you dont get that formating crap
        x=url[:21]+"raw/"+url[21:]
        #print (x) #optional print statment
        try:
            #save the file as the name of the paste it is posible yet not likely that two will have the same name the first one will be overwritten
            z=urllib.request.urlopen(x).read()
            name=url[21:]
            print("[+]creating file "+name+".txt")
            filez=open(path+name+".txt","w")
            filez.write(str(z))
            filez.close()
        except Exception as e: #This catches all exceptions
            #print what went wrong for debugging (optional)
            print("An error occured: "+str(e))
