import logging
import pyodbc
import json
import os
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    connectionstring = os.environ["connectionstring"]
    conn = pyodbc.connect(connectionstring)
    cursor = conn.cursor()

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    topic = req.params.get('topic')
    if not topic:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            topic = req_body.get('topic')

    if name:
        cursor.execute("SELECT * FROM OnlineCourses where Instructor= ? and topic= ?", (name, topic))
    else:
        cursor.execute('SELECT * FROM OnlineCourses')

    # Grab the Records
    records = list(cursor.fetchall())
    logging.info(records)

    #return_body = '  \n '.join([str(elem) for elem in records])
    
    records = [tuple(record) for record in records]
    return_body = json.dumps(obj=records, indent=2)

    return func.HttpResponse(
            body=return_body,
            status_code=200
    )
   
