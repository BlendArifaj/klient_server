#FIEK-TCP_SERVER
#FIEK-TCP_SERVER
def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

def encripto(plaintexti,qelesi):
    ciphertexti =""
    i=0
    while i < len(plaintexti):
      splitArray = list(plaintexti)
      if splitArray[i].isalpha():
         num = ord(splitArray[i])          
         num += qelesi
         if splitArray[i].isupper():
           if num > ord('Z'):
              num -= 26
         elif num < ord('A'):
            num += 26
         elif splitArray[i].islower():
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26
         ciphertexti += chr(num)
         i += 1
      else:
         ciphertexti += splitArray[i]
         i += 1
    return ciphertexti

def dekripto(ciphertexti,qelesi):
    plaintexti =""
    i=0
    while i < len(ciphertexti):
      splitArray = list(ciphertexti)
      if splitArray[i].isalpha():
         num = ord(splitArray[i])          
         num -= qelesi
         if splitArray[i].isupper():
           if num > ord('Z'):
              num -= 26
         elif num < ord('A'):
            num += 26
         elif splitArray[i].islower():
            if num > ord('z'):
                num -= 26
            elif num < ord('a'):
                num += 26
         plaintexti += chr(num)
         i += 1
      else:
         plaintexti += splitArray[i]
         i += 1
    return plaintexti
  
def konverto(konvertimi,temp):
    vleraHyrese = float(temp)
    vleraDalese = 0
    if(konvertimi == "CelsiusToKelvin"):
        vleraDalese = vleraHyrese + 273.15
    elif(konvertimi == "CelsiusToFahrenheit"):
        vleraDalese = (vleraHyrese * 9.0/5) + 32
    elif(konvertimi == "KelvinToFahrenheit"):
        vleraDalese = 9.0/5*(vleraHyrese - 273.15) + 32
    elif(konvertimi == "KelvinToCelsius"):
        vleraDalese = vleraHyrese - 273.15
    elif(konvertimi == "FahrenheitToCelsius"):
        vleraDalese = 5.0/9 * (vleraHyrese - 32)
    elif(konvertimi == "FahrenheitToKelvin"):
        vleraDalese = (vleraHyrese + 459.47) * 5.0/9
    elif(konvertimi == "PoundToKilogram"):
        vleraDalese = 0.45359237 * vleraHyrese
    elif(konvertimi == "KilogramToPound"):
        vleraDalese = vleraHyrese/0.45359237
    MESSAGE = str(vleraDalese)
    conn.send(MESSAGE.encode("ASCII")) 
  
class ClientThread(Thread): 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip
        self.port = port 
   
    def run(self): 
        while True : 
            print ("Serveri eshte i gatshem...")
            data = conn.recv(1024)
            point = data.decode("ASCII")
            points = point.split(' ')
            MESSAGE = points[0]
            print ("Kerkesa e pranuar eshte : "+ data.decode("ASCII"))
            elif points[0]=="FAKTORIEL":
                if points[1].isdigit():
                    MESSAGE = str(factorial(int(points[1])))
                    conn.send(MESSAGE.encode("ASCII"))
                else:
                    MESSAGE = "Ju lutem shkruani numer."
                    conn.send(MESSAGE.encode("ASCII"))
            elif points[0]=="ENKRIPTO":
                try:
                    MESSAGE = "Teksti i enkriptuar : "+encripto(points[1],int(points[2]))
                except:
                    MESSAGE = "Formati EKRIPTO {TEKSTI} {QELESI}"
                conn.send(MESSAGE.encode("ASCII"))
            elif points[0] == "DEKRIPTO":
                try:
                    MESSAGE = "Teksti i dekriptuar : "+dekripto(points[1], int(points[2]))
                except:
                    MESSAGE = "Formati DEKRIPTO {TEKSTI} {QELESI}"
                conn.send(MESSAGE.encode("ASCII"))
            elif points[0]=="KONVERTONUMRAT":
                try:
                 MESSAGE = KonvertoNumrat(points[1],points[2])
                except:
                 MESSAGE = "Ka ndodhur nje gabim gjate shkruarjes se komandes!"
                conn.send(MESSAGE.encode("ASCII"))
            else :
                 MESSAGE = "Ka ndodhur nje gabim. Ju lutem permbahuni komandave te cekura me lart."
                 conn.send(MESSAGE.encode("ASCII")) 
 

TCP_IP = "127.0.0.1"
TCP_PORT = 9000 
BUFFER_SIZE = 1024 
 
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while True: 
    tcpServer.listen(10) 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 
