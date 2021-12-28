import os
import json
import logging

# shared code
from utils import helpers
# azure funcs
import azure.functions as func


# set up logging
logger = logging.getLogger(__name__)

try:
    # API Management logging
    from opencensus.ext.azure.log_exporter import AzureLogHandler
    logger.addHandler(AzureLogHandler())
except Exception as e:
    logger.error(f'Failed to add Azure Log Handler: {e}')
    
def main(req: func.HttpRequest) -> func.HttpResponse:
    
    logger.info(f'req: {req}')
    
    headers = {
        'my-http-header': 'some-value',
        'Content-Type': 'application/json'
        }
    
    name = req.params.get('name')
    
    my_env_var = os.getenv('my_env_var')
    
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    
    if name:
        
        response = {
            'message': f'Hello {helpers.format_name(name)}!',
            'my_env_var': my_env_var
        }
        
        return func.HttpResponse(json.dumps(response), headers=headers)
    
    else:
        return func.HttpResponse(
             'Please pass a name on the query string or in the request body',
             headers=headers, status_code=400
        ) 
        

if __name__ == "__main__":
    main()