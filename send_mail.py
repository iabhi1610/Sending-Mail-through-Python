import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
username = 'tesy28677@gmail.com'
password = 'test12!@' 




def send_mail(text='Email Body', subject='Experimental Mail',from_email = 'Tester <tesy28677@gmail.com>', to_emails=None, html=None):
    assert isinstance(to_emails, list) #assert -> raise an error if it's not a list.
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    if html != None:
        html_part = MIMEText("<h1>This is working</h1>", 'html')
        msg.attach(html_part)
    msg_str = msg.as_string()
    #login to my smtp server
    server =  smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()
