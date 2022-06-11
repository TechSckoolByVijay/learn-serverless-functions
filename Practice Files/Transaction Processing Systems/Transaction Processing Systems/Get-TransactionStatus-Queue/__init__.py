import logging

import azure.functions as func


def main(req: func.HttpRequest, outputSbMsg: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Getting the paramter values from http request
        UserName = req.params.get('UserName')
        CourseID = req.params.get('CourseID')
        TransactionStatus = req.params.get('TransactionStatus')
        User_Email = req.params.get('User_Email')

        if UserName and CourseID and TransactionStatus and User_Email:
            addMsgToQueue = """{
                    "UserName":"%s", 
                    "CourseID":"%s",
                    "TransactionStatus":"%s",
                    "User_Email":"%s"
                } """ % (UserName,CourseID,TransactionStatus,User_Email)
            logging.info(addMsgToQueue)

            # Writing the message to queue with the help of output binding
            outputSbMsg.set(addMsgToQueue)
            
            return func.HttpResponse("Message Received")
        else:
            logging.info('Request Failed as one or more parameter are missing in the http call.')
            return func.HttpResponse("Request Failed as one or more parameter are missing in the http call.")
    except:
        return func.HttpResponse("Something went wrong")
   