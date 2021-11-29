from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pss




def generarLlaves():
    nombres = ['Betito', 'Alicia', 'Candy']

    for j in nombres:
        key = RSA.generate(1024)
        name_priv = 'llaveprivada' + j + ".der"
        name_pub = 'llavepublica' + j + ".der"
        llave_privada = key.exportKey()

        privada = open(name_priv, 'wb')
        privada.write(llave_privada)
        privada.close()

        keypub = key.public_key().export_key()
        publica = open(name_pub, 'wb')
        publica.write(keypub)
        publica.close()

def txtToBytes(ruta):
    archivo = open(ruta, "rb")
    texto = archivo.read()
    archivo.close()
    return texto
def imprimirFirma(contenido, rutaAGuardarFirmado):
    arc = open(rutaAGuardarFirmado, 'wb')
    arc.write(contenido)
    arc.close()

def firma(rutaTxtMensajeOrigial, rutaLlavePrivada):
    message = txtToBytes(rutaTxtMensajeOrigial)
    key = RSA.import_key(open(rutaLlavePrivada).read())
    h = SHA256.new(message)
    signature = pss.new(key).sign(h)
    contenido_firma = signature + message
    imprimirFirma(contenido_firma, rutaArchivoFirmadoNuevo)
    print ("archivo firmado con exito")


def verificar(rutatxt, rutaLlavepublica):
    bytesVerificar = open(rutatxt, 'rb').read()
    key = RSA.import_key(open(rutaLlavepublica, 'rb').read())
    h = SHA256.new(bytesVerificar[128:])
    verifier = pss.new(key)
    try:
        verifier.verify(h, bytesVerificar[0:128])
        print ("La firma es autentica")
    except (ValueError, TypeError):
        print ("La firma no es autentica")











