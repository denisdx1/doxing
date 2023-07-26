import requests
import json
import base64
import signal
from PIL import Image

#colores
YL = "\033[33;1m"
CNL = '\033[35m'
VL = "\033[32;1m"
WL = "\033[0;1m"

def trap_c(sig, frame):
    print(YL+"\nSALIENDO....")
    exit()
  
signal.signal(signal.SIGINT, trap_c)

class MethodRequest():

    def __init__(self):
        self.URL = "https://d4vid0day.pythonanywhere.com/Reniec/api/basica/dni="
        self.Request_r = requests.session()

    def sendGetUrl(self):
        try:
            sendDni = int(input(f"{VL}[DNI] {CNL}-> {WL}"))
        except ValueError:
            print(YL+"INGRESE UN DNI")
            return main.sendGetUrl()

        if len(str(sendDni)) == 8:
            headers_send = {
                "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:108.0) Gecko/20100101 Firefox/108.0",
                "Content-Type": "application/json"
            }
            apiUrl = self.URL + str(sendDni)
            sendResponse = self.Request_r.get(apiUrl, headers=headers_send)

            if sendResponse.status_code == 200:

                try:
                    typingJson = sendResponse.json()['data']['persona']
                    nombre = typingJson['prenombres']
                    apellidoPa = typingJson['apPrimer']
                    apellidoMa = typingJson['apSegundo']
                    estado = typingJson['estadoCivil']
                    restric = typingJson['restriccion']
                    dire = typingJson['direccion']
                    ubi = typingJson['ubigeo']
                    foto = typingJson['foto']
                    decodeIMG = open(f'{sendDni}.jpg', 'wb')
                    decodeIMG.write(base64.b64decode((foto)))
                    decodeIMG.close()
                    print(f"{VL}NOMBRE: {WL}{nombre}\n{VL}APELLIDO PATERNO: {WL}{apellidoPa}\n{VL}APELLIDO MATERNO: {WL}{apellidoMa}\n{VL}ESTADO: {WL}{estado}")
                    print(f"{VL}RESTRICCIÓN: {WL}{restric}\n{VL}DIRECCIÓN: {WL}{dire}\n{VL}UBIGEO: {WL}{ubi}")

                    # Abrir la imagen automáticamente
                    img = Image.open(f'{sendDni}.jpg')
                    img.show()

                except KeyError:
                    print("EL DNI NO EXISTE O ES DE UN MENOR")

            else:
                print(YL+"OCURRIO UN ERROR [%S]" % (sendResponse.status_code))    
        else:
            print(YL+"INGRESE UN DNI VALIDO")       
   
main = MethodRequest()
main.sendGetUrl()
