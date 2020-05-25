
import os
import smtplib
import imghdr
from email.message import EmailMessage

class email:
    email_id = ""
    password = ""
    sender_email_id = ""
    person_name = ""
    type_loan = ""
    phone_number = ""


    def __init__(self,email_id,password,sender_email_id,person_name,type_loan,phone_number):
        self.email_id = email_id
        self.password = password
        self.sender_email_id = sender_email_id
        self.type_loan = type_loan
        self.phone_number = phone_number
        self.person_name = person_name

    def sendmail(self):
        EMAIL_ADDRESS = self.email_id 
        EMAIL_PASSWORD = self.password

        #contacts = ['YourAddress@gmail.com']

        msg = EmailMessage()
        msg['Subject'] = 'Coustmers details'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = self.sender_email_id

        msg.set_content('')

        htmlfile =""" \
        <!DOCTYPE html>
        <html>
        <head>
        <link rel="stylesheet" type="text/css" href="/home/harshith/Desktop/mail/style.css">
        </head>
        <body>
        <p>This is the mail reagrding lates enquirey with the coustmers</p>

        <h2>Coustmer Detials</h2>

        <table>
        <tr>
            <th>Person Name</th>
            <th>Email id</th>
            <th>Type Loan</th>
            <th>Phone Number</th>
        </tr>
        <tr>
            <td>{person_name:}</td>
            <td>{email_id:}</td>
            <td>{type_loan:}</td>
            <td>{phone_number:}</td>
        </tr>
        </table>

        </body>
        </html>
                """

        msg.add_alternative("/home/harshith/Desktop/mail/style.css",subtype ="css")

        htmlfile = htmlfile.format(person_name=self.person_name,email_id =self.sender_email_id,type_loan= self.type_loan,phone_number=self.phone_number )
        msg.add_alternative(htmlfile, subtype='html')


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("message  has been send succesfully")


