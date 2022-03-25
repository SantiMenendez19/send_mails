import smtplib
import getpass
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import sys

# Funcion de envio de mail
def send_mail(
    sender_mail,
    receptor_mail_list,
    subject,
    message,
    attachments_list=[],
    server_smtp="AWSSES",
    server_host_smtp="",
    user_host_smtp="",
    env_pass="PASSWORD_SMTP",
):
    """Funcion que envia un mail a una lista de destinatarios.
    :param sender_mail: Correo electronico del remitente.
    :param receptor_mail_list: Lista de correos electronicos de los destinatarios.
    :param subject: Asunto del mail.
    :param message: Mensaje del mail.
    :param attachments_list: Lista de archivos adjuntos.
    :param server_smtp: Servidor SMTP.
    :param env_pass: Variable de entorno que contiene la contraseña. Si es None se le solicitara en la consola.
    :return: None
    """
    if server_smtp == "GMAIL":
        # SMTP Gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)
    elif server_smtp == "OFFICE365":
        # SMTP Office 365
        server = smtplib.SMTP("SMTP.Office365.com", 587)
    elif server_smtp == "AWSSES":
        server = smtplib.SMTP(server_host_smtp, 587)
    try:
        if env_pass is not None:
            password = os.environ[env_pass]
        else:
            return 1  # Error no hay contraseña
            # password = getpass.getpass("Ingrese password: ")
        server.starttls()
        if server_smtp == "AWSSES":
            server.login(user_host_smtp, password)
        else:
            server.login(sender_mail, password)
        # Armado del mensaje
        msg = MIMEMultipart()
        msg["From"] = sender_mail
        msg["To"] = ",".join(receptor_mail_list)
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))
        # Envio de adjuntos
        if len(attachments_list) > 0:
            for filepath in attachments_list:
                attachment = MIMEApplication(open(filepath, "rb").read())
                attachment.add_header(
                    "Content-Disposition",
                    "attachment",
                    filename=os.path.basename(filepath),
                )
                msg.attach(attachment)
        # Enviar mail
        print(f"Se enviara el mail a la direccion: {receptor_mail_list}")
        server.sendmail(msg["From"], receptor_mail_list, msg.as_string())
        print(f"El mensaje se envio correctamente a la direccion {receptor_mail_list}")
        server.quit()
        return 0
    except Exception as err:
        print("Error: " + str(err))
        server.quit()
        return 1

# Main
if __name__ == "__main__":
    # Parametros de mail
    emisor_mail = "anon@mail.com"
    receptor_mail = ["receiver@anon.com"]
    asunto_mail = "Prueba Python Mails"
    # Mensaje a enviar
    mensaje = "Hola, pruebo lo de Python"

    # Archivo adjunto
    adjunto = [os.path.join(os.path.dirname(sys.argv[0]), "Adjunto", "dummy")]

    send_mail(emisor_mail, receptor_mail, asunto_mail, mensaje, adjunto, "GMAIL", None)