import csv

def cesar(mensaje, clave):
    abc = "abcdefghijklmnopqrstuvwxyz"
    abc_mayus = "ABCDEFGHIJkLMNOPQRSTUVWXYZ"
    longitud = len(abc)
    codificar = ""

    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == "ñ":
            codificar += letra
            continue
        valor_letra = ord(letra)
        usar_abc = abc
        limite = 97
        if letra.isupper():
            limite = 65
            usar_abc = abc_mayus
        
        posicion = (valor_letra - limite + clave) % longitud
        codificar += usar_abc[posicion]

    return codificar
    

def atbash(mensaje):
    abc = "abcdefghijklmnopqrstuvwxyz"
    abc_mayus = "ABCDEFGHIJkLMNOPQRSTUVWXYZ"
    longitud = len(abc)
    codificar = ""

    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == "ñ":
            codificar += letra
            continue
        valor_letra = ord(letra)
        usar_abc = abc
        limite = 97
        if letra.isupper():
            limite = 65
            usar_abc = abc_mayus
        
        posicion = longitud - (valor_letra - limite + 1)
        codificar += usar_abc[posicion]

    return codificar

def atbash_descifrar(mensaje):
    abc = "abcdefghijklmnopqrstuvwxyz"
    abc_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    descifrado = ""

    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == "ñ":
            descifrado += letra
            continue
        usar_abc = abc
        if letra.isupper():
            usar_abc = abc_mayus
        
        posicion = usar_abc.index(letra)
        letra_descifrada = usar_abc[-(posicion + 1)]
        descifrado += letra_descifrada
    
    return descifrado

def validar_identificador(destinatario):
    caracteres_validos = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789_-."
    min_caracteres = 5
    max_caracteres = 15

    if min_caracteres <= len(destinatario) <= max_caracteres:
            for caracter in destinatario:
                if caracter not in caracteres_validos:
                    return False
            return True
    return False

def cifrar_mensajes():
    mensaje = str(input("Ingrese el mensaje que desea cifrar: "))
    print("Que cifrador desea usar?")
    print("", "1) Cesar", "\n", "2) Atbash")
    opcion = int(input())
    if opcion == 1:
            clave = int(input("Que clave desea utilizar para el cifrado Cesar: "))
            mensaje_cifrado = cesar(mensaje, clave)
            print("Su mensaje cifrado es:", mensaje_cifrado, "\n")
            print("Mensaje Enviado", "\n")
            return f"C{clave}", mensaje_cifrado
        
    elif opcion == 2:
            mensaje_cifrado = atbash(mensaje)
            print("Su mensaje cifrado es:", mensaje_cifrado, "\n")
            print("Mensaje Enviado", "\n")
            return "A", mensaje_cifrado

def guardar_mensajes_encriptados(destinatario, cifrador, mensaje_cifrado):
    row = [destinatario, cifrador, mensaje_cifrado]
    salida = open("semana 7/mensajes_cifrados.csv", "a")
    csvwriter = csv.writer(salida)
    csvwriter.writerow(row)

def desencriptar():
    archivo = open("semana 7/mensajes_cifrados.csv", "r")
    csvreader = csv.DictReader(archivo)
    resultado = []
    for row in csvreader:
        mensaje_a_descifrar = row["mensaje-cifrado"]
        cifrado = row["cifrado"]
        if cifrado.startswith("C"):
            clave = int(cifrado[1:])
            mensaje_ya_descifrado = cesar(mensaje_a_descifrar, clave * -1)

        elif cifrado == "A":
            mensaje_ya_descifrado = atbash_descifrar(mensaje_a_descifrar)
        destinatario = row["destinatario"]
        resultado.append((destinatario, mensaje_ya_descifrado))
    archivo.close()
    return resultado

def identificador_espia():
    identificar = str(input("Ingrese su identificador de espía: "))
    print("")
    if validar_identificador(identificar) == True or identificar == "*":
            mostrar_mensajes_encriptados(identificar)
            print("Total de mensajes:", contador_mensajes(), "\n")
            return main()
    else:
            print("ALERTA: Usted es un intruso", "\n")
            return main()

def mostrar_mensajes_encriptados(identificar):
    mensajes = desencriptar()
    espia = identificar
    print("Lista de mensajes: ")
    print("-" * 120)
    for destinatario, mensaje in mensajes:
        if destinatario == "*":
            print("TODOS:", mensaje)
            print("-" * 120)
    
    for destinatario, mensaje in mensajes:
        if destinatario in espia:
            print(destinatario.upper()[:3] + ":", mensaje)
            print("-" * 120)

def contador_mensajes():
    archivo = open("semana 7/mensajes_cifrados.csv", "r")
    csvreader = csv.DictReader(archivo)
    contador = 0
    for row in csvreader:
        contador += 1
    archivo.close()
    return contador

try:
    def main():
        print("Cifrador de mensajes")
        print("Que desea hacer?")
        print("", "1) Cifrar mensaje", "\n", "2) Descifrar mensaje", "\n", "3) Enviar mensaje cifrado", "\n", "4) Consultar mensajes cifrados")
        select = int(input())

        if select == 1:
            cifrar_mensajes()
            return main()
        
        elif select == 2:
            mensaje = str(input("Ingrese el mensaje que desea descifrar: "))
            print("Que cifrador desea usar?")
            print("", "1) Cesar", "\n", "2) Atbash")
            opcion = int(input())
            if opcion == 1:
                clave = int(input("Que clave desea utilizar para el cifrado Cesar: "))
                print("Su mensaje descifrado es:", cesar(mensaje, clave), "\n")
                return main()
            
            elif opcion == 2:
                print("Su mensaje descifrado es:", atbash_descifrar(mensaje), "\n")
                return main()
        
        elif select == 3:
            destinatario = str(input("Ingrese el espía destinatario del mensaje: "))
            if validar_identificador(destinatario) == True or destinatario == "*" :
                opcion, mensaje_cifrado = cifrar_mensajes()
                guardar_mensajes_encriptados(destinatario, opcion, mensaje_cifrado)
            else:
                print("Espía Inexistente", "\n")
            return main()
        
        elif select == 4:
            identificador_espia()      

    main()
except ValueError:
    print("Opcion invalida. Intente nuevamente. \n")
    main()