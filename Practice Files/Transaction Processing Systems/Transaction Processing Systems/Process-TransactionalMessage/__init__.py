import logging
import json
import os
import pyodbc
import azure.functions as func
import smtplib, ssl

def main(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))


    # Grabbing the message from azure service bus queue and converting it into JSON
    message_json_string = msg.get_body().decode('utf-8')
    json_data = json.loads(message_json_string)


    # Getting values out of JOSN object
    UserName = json_data['UserName']
    CourseID = json_data['CourseID']
    TransactionStatus = json_data['TransactionStatus']
    User_Email = json_data['User_Email']

    insert_data = (UserName,CourseID,TransactionStatus,User_Email)

    connectionstring = os.environ["connectionstring"]
    conn = pyodbc.connect(connectionstring)
    cursor = conn.cursor()

    if TransactionStatus == 'SUCCESS':
        cursor.execute("INSERT INTO StudentsData (UserName, CourseID, TransactionStatus, User_Email ) VALUES (?, ?, ?, ? )", insert_data)
    else:
        cursor.execute("INSERT INTO FailedToConvert (UserName, CourseID, TransactionStatus, User_Email ) VALUES (?, ?, ?, ? )", insert_data)
    
    conn.commit()

    # Database Operation End 


    # Sending Email
    
    mailTo = User_Email
    if TransactionStatus == 'SUCCESS':
        subject = "Good News | You are In"
        content = "Your request is successfully accepted \n Welcomw to Vijay's course \n Regards"
    else:
        subject = "Transaction Declined"
        content = "Appologies. Transaction failed \n We will get back to you soon \n Regards"

    smtp_server_domain_name="smtp.gmail.com"
    port=465
    sender_mail="techsckool@gmail.com"
    password="yutnauqqnwznyows"

    # Sending Email using gmail smtp server
    ssl_context = ssl.create_default_context()
    service = smtplib.SMTP_SSL(smtp_server_domain_name, port, context=ssl_context)
    service.login(sender_mail, password)
    result = service.sendmail(sender_mail, mailTo, f"Subject: {subject}\n{content}")
    service.quit()

    # End of function 