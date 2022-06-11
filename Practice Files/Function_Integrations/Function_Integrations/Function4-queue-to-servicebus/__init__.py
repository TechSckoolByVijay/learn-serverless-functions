import logging

import azure.functions as func


def main(msg: func.QueueMessage, outputSbMsg: func.Out[str]) -> None:
    logging.info('Python queue trigger function processed a queue item: %s',
                 msg.get_body().decode('utf-8'))

    clear_text = msg.get_body().decode('utf-8')
    sendMessageOut = "Processed by Func4 \n" +  clear_text

    outputSbMsg.set(sendMessageOut)