import logging
from multiprocessing import connection
import pyodbc
import os
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    connectionstring = os.environ["connectionstring"]
    conn = pyodbc.connect(connectionstring)
    cursor = conn.cursor()
  
    ReviewText = req.params.get('review')
    if not ReviewText:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            ReviewText = req_body.get('review')
    
    if ReviewText:
        cursor.execute("INSERT INTO StudentReviews (ReviewTime, ReviewText) VALUES (CURRENT_TIMESTAMP, ?)", ReviewText )
    else:
        cursor.execute("INSERT INTO StudentReviews (ReviewTime, ReviewText)  VALUES (CURRENT_TIMESTAMP, 'BAD_RECORD')")
    
    conn.commit()
        
    # Prepare & Return the HTTP Response
    return func.HttpResponse(
                body="Your request is processed",
                status_code=202
        )
        
    
    