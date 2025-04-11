import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Test message'
msg['From'] = 'from@mail.local'
msg['To'] = ', '.join(['to@mail.local'])
msg.set_content('Hello')

server = smtplib.SMTP('192.168.0.50', 1025)
server.set_debuglevel(1)
server.send_message(msg)
server.quit()
