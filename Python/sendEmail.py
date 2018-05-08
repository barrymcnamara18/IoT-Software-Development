## Code Reused from https://github.com/DexterInd/GrovePi/blob/master/Projects/Send_Email_With_Pi/sendemailtls.py

SMTPserver = 'smtp.gmail.com'		#Set the SMTP server to send emails from
sender =     'iotrasp141@gmail.com'				#Email account setup for testing the project
sendTo = ['barrybmcnamara@gmail.com']	#Send the emails to my email address

USERNAME = sender
PASSWORD = "368XvEh9#DXu@CF98^RNgEGT"

#Setting the message format to plain text 
text_subtype = 'plain'

content="""\
Test message
"""

import sys
import os
import re

# from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
from smtplib import *
from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)
from email.MIMEText import MIMEText


def send_email(content, sendTo, subject):
    try:
        msg = MIMEText(content, text_subtype)
        msg['Subject']=       subject
        msg['From']   = sender # some SMTP servers will do this automatically, not all

        # timeout is critical here for long term health.  
        conn = SMTP(SMTPserver, port = 587, timeout = 60)
        
        conn.ehlo()
        conn.starttls()
        conn.ehlo()
        conn.login(USERNAME, PASSWORD)
        conn.set_debuglevel(1)
        try:
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.close()

sys.exit()

    except Exception as exc:
        print("Mail failed; %s" % str(exc))
        print("Moving on!")