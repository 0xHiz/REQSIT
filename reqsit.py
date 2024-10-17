import requests as req
from time import sleep

V = '\033[1;97m' # ابيض
Z = '\033[1;31m' #احمر
S = '\033[1;33m' #اصفر
R = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
          

print(V+" /$$$$$$$  /$$$$$$$$  /$$$$$$    /$$$$$$  /$$$$$$ /$$$$$$$$ ")
print(Z+"| $$__  $$| $$_____/ /$$__  $$  /$$__  $$|_  $$_/|__  $$__/ ")
print(S+"| $$  \ $$| $$      | $$  \ $$ | $$  \__/  | $$     | $$    ")
print(R+"| $$$$$$$/| $$$$$   | $$  | $$ |  $$$$$$   | $$     | $$    ")
print(F+"| $$__  $$| $$__/   | $$  | $$  \____  $$  | $$     | $$    ")
print(A+"| $$  \ $$| $$      | $$/$$ $$  /$$  \ $$  | $$     | $$    ")
print(C+"| $$  | $$| $$$$$$$$|  $$$$$$/ |  $$$$$$/ /$$$$$$   | $$    ")
print(B+"|__/  |__/|________/ \____ $$$  \______/ |______/   |__/    ")
print(Y+"                          \__/                              ")

FileName = input("Enter File Name >> ")
FileSites = open(FileName,"r")

readFile = FileSites.readlines()

lineN = 1

for x in readFile :
    try :
        x = x.replace("\n","")
        respons_code = req.get(x).status_code
        if respons_code == 200 :
            print(f"{F}{lineN}- {x} --> {respons_code}")
        elif  respons_code == 404 :
            print(f"{Z}{lineN}- {x} --> {respons_code}")
        else :
            print(f"{S}{lineN}- {x} --> {respons_code}")
        lineN += 1
    except :
        print(f"{Z}{lineN}- {x}")
        lineN += 1
        continue

FileSites.close()
    
