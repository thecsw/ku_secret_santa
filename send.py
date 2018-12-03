#!/bin/env python

"""
KU Secret Santa
"""

import smtplib

from tqdm import tqdm

import config
import message

SERVER = smtplib.SMTP('smtp.gmail.com:587')
SERVER.ehlo()
SERVER.starttls()
SERVER.login(config.USERNAME, config.PASSWORD)

def send_mail(toaddr, msg):
    """
    Takes an address and a string. Just sends mail
    """
    SERVER.sendmail(config.FROM_ADDRESS, toaddr,
                    message.modify_message(msg, toaddr))

def main():
    """
    This is where the magic happens
    """
    emails = []
    with open("users.txt", "r") as r:
        emails = [x.replace('\n', '') for x in r.readlines()]

    targets = []
    with open("targets.txt", "r") as r:
        targets = [x.replace('\n', '') for x in r.readlines()]

    user_input = input(f"Send the message to {len(emails)} recipients? (Y/n): ")
    if user_input != 'Y':
        print("Abort.")
        SERVER.quit()
        exit()

    for email in enumerate(emails):
        send_mail(email[1], message.modify_reveal(targets[email[0]]))
        print(email[1] + " -> " + targets[email[0]])
    SERVER.quit()

if __name__ == '__main__':
    main()
