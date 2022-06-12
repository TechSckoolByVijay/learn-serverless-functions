import logging

import azure.functions as func


def main(myblob: func.InputStream, outputBlob: func.Out[str]) -> None:
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    
    clear_text = myblob.read().decode('utf-8')
    #logging.info("Clear text:%s'", clear_text)

    outputBlob.set(clear_text)