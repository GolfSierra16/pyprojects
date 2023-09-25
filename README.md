# pyprojects
"Mensajes Secretos"\
Este es uno de los proyectos que realizamos durante nuestra capacitación. Consiste en un pequeño programa dividido en 4 secciones:

1: Cifrar mensaje\
  El usuario ingresa el texto a cifrar, y el programa pregunta cuál cifrador usar. En este caso, entre los métodos César y Atbash.

2: Descifrar mensaje\
  El usuario ingresa el texto cifrado, y el programa pregunta el método de cifrado utilizado anteriormente.

3: Enviar mensaje cifrado\
  El funcionamiento es igual a la opción 1, agregándole la capacidad de enviar ese mensaje a un usuario en particular.\
  El mensaje se guarda en un archivo .CSV, junto con el usuario destinatario y el cifrador utilizado.

4: Consultar mensajes cifrados\
  El usuario ingresa su identificador. Si el identificador no está presente en el .CSV el acceso se le denegará y volverá al menú principal.\
  Si la identificación es positiva, la consola mostrará la lista de mensajes, al mismo tiempo que los descifra, listándolos de la siguiente manera:\
    En primer lugar, los mensajes de comunicación general.\
    En segundo lugar, los mensajes dirigidos al identificado.
