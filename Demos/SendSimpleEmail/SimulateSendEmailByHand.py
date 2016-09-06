# -*- coding: utf-8 -*-
# https://github.com/SavinaRoja/PyUserInput/wiki/Installation
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

# only support English for now.
def send_mail(mail_server, mail_user, mail_pass, mail_to, subject, content):
    print("send_mail")
    try:
        # click send mail button
        m.click(1920 + 162, 107)
        time.sleep(2)

        # click input send to
        m.click(1920 + 260, 163)
        time.sleep(1)
        k.type_string(mail_to)
        time.sleep(1)

        # click input theme, click twice avoid the user info dialog break our logic
        m.click(1920 + 260, 206)
        time.sleep(1)
        m.click(1920 + 260, 206)
        time.sleep(1)
        k.type_string(subject)
        time.sleep(1)

        # click input content
        m.click(1920 + 260, 350)
        time.sleep(1)
        k.type_string(content)
        time.sleep(1)

        # click send mail
        m.click(1920 + 140, 118)
        time.sleep(1)

        # back to home
        m.click(1920 + 80, 68)
        time.sleep(2)
        return True
    except:
        return False