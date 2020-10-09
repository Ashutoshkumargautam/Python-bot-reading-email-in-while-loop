from time import sleep
import imaplib
import time
import sys
import email

email_address = 'xyzxxxaxbxzx123@gmail.com' 
email_pass = 'xxx@123456'

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(email_address, email_pass)

num_of_mail = 0

while True:
   
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

