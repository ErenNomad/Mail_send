import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

message = MIMEMultipart()
message["From"] = "from who"
message["To"] = "person to be sent"             
message["Subject"]= "Smt mail sends"
text = """
Enter the text                                    #ErenNomad
    """
  
message_body = MIMEText(text,"plain")
mesaj.attach(mesaj_govdesi)
try:
    mail = smtplib.SMTP("smptp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("Enter sender mail","Enter sender mail password")
    mail.sendmail(["From"],message["To"],message.as_string())
    print("Email sent successfully")
    mail.close()
except:
    sys.stderr.write("An error occurred while running the program.")
    sys.stderr.flush()
