#===================================[program logic]============================================#
""" When new email comes then bot will capture that email and doing work it own way
    if any email is not coming so that time bot will waitting for intire time."""
#================================================================================================#
from time import sleep
import imaplib, email
import time
import sys
#===============================================================================>>
#=============[Reading email here..]===============================>>
import imaplib
import email

email_address = 'xyzxxxaxbxzx123@gmail.com' # Placeholder
email_pass = 'xxx@123456' # Placeholder

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(email_address, email_pass)

num_of_mail = 0

while True:
    # ==================================================================================================================>>>
    # 2nd -> if any email is not comming in bot email box then wait  infinite time....
    print("Waitting for website response...")

    # animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
    mail.select('inbox')

    type, data = mail.search(None, '(UNSEEN)')
    mail_ids = data[0]
    id_list = mail_ids.split()

    if len(id_list) > num_of_mail:
        # ================================================================================>>
        # 1st -> if any new email came in bot email box then read that email and cature all information inside email...
        print('New Mail Found...\n')

        for i in range(int(id_list[-1]), int(id_list[0]) -1, -1):
            typ, data = mail.fetch(i, '(RFC822)')

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    email_body = msg.get_payload()[0].get_payload()
                    file = open('EMAIL.txt','w')
                    file.write(email_from)
                    file.write(email_subject)
                    file.write(email_body)
                    file.close()
        num_of_mail = len(id_list)

