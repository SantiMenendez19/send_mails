import smtplib
import getpass
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import sys

#Parametros de mail
emisor_mail = "anon@mail.com"
receptor_mail = ["receiver@anon.com"]
asunto_mail = "Prueba Python Mails"

#Mensaje a enviar
mensaje = "Hola, pruebo lo de Python"

#Usando modulo email
msg = MIMEMultipart()

# Descomentar el servicio de mail a utilizar
#SMTP Office 365
server = smtplib.SMTP("SMTP.Office365.com",587)
#SMTP Gmail
#server = smtplib.SMTP("smtp.gmail.com",587)

#Password
#password = getpass.getpass("Ingrese password: ")

#Envio de mail
try:
    password = getpass.getpass("Ingrese password: ")
    lista = open(os.path.dirname(sys.argv[0]) + "/lista_test.txt",encoding="utf8") #Uso una lista de mails
    server.starttls()
    server.login(emisor_mail,password)
    for dir in lista:
        #Armado del mensaje
        msg = MIMEMultipart()
        msg['From'] = emisor_mail
        receptor_mail = [dir]
        msg['To'] = ','.join(receptor_mail)
        msg['Subject'] = asunto_mail
        msg.attach(MIMEText(mensaje, 'plain'))
        #Envio de adjuntos
        path = os.path.dirname(sys.argv[0])
        path_adjunto = path+"/adjunto/"
        for (_,_,arch) in os.walk(path_adjunto):
            for archivo in arch:
                part = MIMEApplication(open(path_adjunto+"/"+archivo,"rb").read())
                part.add_header('Content-Disposition', 'attachment', filename=archivo)
                msg.attach(part)
        #Enviar
        print("Se enviara el mail a la direccion: " + dir,end="")
        server.sendmail(msg['From'],receptor_mail, msg.as_string())
        print("El mensaje se envio correctamente a la direccion " + dir,end="")
except Exception as e:
   print("Error: "+ str(e))
server.quit()
