import os
import json
import logging
import azure.functions as func
from utils import helpers

from opencensus.extension.azure.functions import OpenCensusExtension
from opencensus.trace import config_integration
config_integration.trace_integrations(['requests'])
OpenCensusExtension.configure()



def main(
        req: func.HttpRequest,
        context: func.Context
    ) -> func.HttpResponse:
    
    logging.info(f'req: {req}')
    logging.info(f'context: {context}')
    
    headers = {"my-http-header": "some-value"}
    
    name = req.params.get('name')
    
    my_env_var = os.environ["my_env_var"]
    
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
             "Please pass a name on the query string or in the request body",
             headers=headers, status_code=400
        ) 