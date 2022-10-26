#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from email.message import EmailMessage
import ssl
import smtplib
message_to_Send = "Hi this is Xxxx"
em=EmailMessage()

#Enter from address
em["From"]= "from_address@email.com"
#Enter To address
em["To"]="to_address@email.com"
#Email subject
em["Subject"]="your subject"
em.set_content(message_to_Send)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    #password should be the authenticated from google authentication for safety
    smtp.login("from_address@email.com","your_password")
    smtp.sendmail("from_address@email.com","to_address@email.com",em.as_string())

