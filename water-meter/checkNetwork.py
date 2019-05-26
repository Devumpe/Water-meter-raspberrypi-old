import urllib.request 
from subprocess import Popen
def internet_on():
    try:
        urllib.request.urlopen("http://www.google.com/")
        print("yes")
        Popen(["python3", "upImage.py"])

    except urllib.error.URLError as err:
        i=0
        text_file = open('data.txt','r')
        line = text_file.read().splitlines()
        
        textdate = line[i]
        textrfid = line[i+1]
        textimage = line[i+2]
        text_file.close()
        nwtext_file = open('nwdata.txt','a')
        nwtext_file.write(textdate +'\n')
        nwtext_file.write(textrfid +'\n')
        nwtext_file.write(textimage + '\n')
        text_file.close()
        
        print("No")
        pass

internet_on()
