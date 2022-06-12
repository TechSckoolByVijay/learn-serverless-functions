import logging

import azure.functions as func


def main(myblob: func.InputStream, outputQueueItem: func.Out[str]) -> None:
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    outputQueueItem.set(myblob.read().decode('utf-8'))
