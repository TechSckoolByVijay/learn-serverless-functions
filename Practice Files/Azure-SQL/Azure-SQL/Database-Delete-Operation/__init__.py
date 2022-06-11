import datetime
import logging
import pyodbc
import os
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    connectionstring = os.environ["connectionstring"]
    conn = pyodbc.connect(connectionstring)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM StudentReviews Where ReviewText='BAD_RECORD'")
    conn.commit()

    logging.info("Rows Deleted = %s", cursor.rowcount)
    logging.info('Scheduled task completed')
