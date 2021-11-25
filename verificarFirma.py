from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

nombre='Betito'
def leerArchivo(nombre):
    ruta = 'textoFirmado' + nombre + ".txt"
    bytesTxt = open(ruta, "rb")
    bytesOG = bytesTxt.read()
    bytesTxt.close()
    return bytesOG

def descifrarRSA(nombre, bytesRSA):
    ruta = 'LlavesPublicas/llavepub' + nombre + ".pem"
    tam = len(bytesRSA)
    print (str(bytesRSA[0:23]))
    h = SHA256.new(bytesRSA[0:23])
    key = RSA.import_key(open(ruta).read())
    try:
        pkcs1_15.new(key).verify(h, bytesRSA[24:] )
        print ("Mensaje verificado")
    except:
        print ("Firma no valida")

bytesOG = leerArchivo(nombre)
descifrarRSA(nombre, bytesOG)