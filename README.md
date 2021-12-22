# send_mails

## Descripcion

Proyecto corto de envio de mails hecho en Python.
El Script permite enviar mails utilizando el STMP de outlook o gmail a una lista de mails con archivos adjuntos.

## Parametros

Los parametros a configurar dentro de la funcion son:

- sender_mail: Correo electronico del remitente. Ejemplo: "anon@mail.com"
- receptor_mail_list: Lista de correos electronicos de los destinatarios.
- subject: Asunto del mail.
- message: Mensaje del mail.
- attachments_list: Lista de archivos adjuntos.
- server_smtp: Servidor SMTP.
- env_pass: Variable de entorno que contiene la contraseña. Si es None se le solicitara en la consola.
