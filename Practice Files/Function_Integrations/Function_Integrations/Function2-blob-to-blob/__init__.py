import logging
from shared_code import common_functions
import azure.functions as func


def main(myblob: func.InputStream, outputBlob: func.Out[str]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    clear_text = myblob.read().decode('utf-8')
    sendMessageOut = "Processed by Func2 \n" +  clear_text

    outputBlob.set(sendMessageOut)


    # Fetching the name of blob
    # myblob.name -> containername/blobname --> container-1/0b84aff1-a79f-4345-96f9-62ec8b86095f
    tmp = (myblob.name).split("/")
    containerName = tmp[0]
    blobName = tmp[1]

    logging.info(f"Calling the delete method on blob ")
    common_functions.delete_blob(containerName, blobName)