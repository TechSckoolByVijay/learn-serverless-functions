import logging

import azure.functions as func


def main(msg: func.QueueMessage, outputSbMsg: func.Out[str]) -> None:
    logging.info('Python queue trigger function processed a queue item: %s',
                 msg.get_body().decode('utf-8'))

    outputSbMsg.set( msg.get_body().decode('utf-8') )
