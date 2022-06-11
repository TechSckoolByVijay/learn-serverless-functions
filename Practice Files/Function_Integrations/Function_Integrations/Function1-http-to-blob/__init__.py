import logging

import azure.functions as func


def main(req: func.HttpRequest, outputBlob: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    message = req.params.get('message')
    sendMessageOut = "Processed by Func1 \n" +  message
    
    outputBlob.set( sendMessageOut )

    return func.HttpResponse(f"Thank You")
