import sys
import os
import logging
import json

# Add the project root to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.append(project_root)

from com.dimcon.synthera_netsuite_integration.utilities.responses import ResponseBuilder
from com.dimcon.synthera_netsuite_integration.services.account_api import account_api

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info(f"Lambda event: {json.dumps(event)}")
    
    http_method = event.get("httpMethod")
    resource_path = event.get("resource")
    if resource_path is None:
        return ResponseBuilder.build_response(400, {"error": "Missing 'resource' in event."})
    if http_method is None:
        return ResponseBuilder.build_response(400, {"error": "Missing 'httpMethod' in event."})
    
    path_params = event.get("pathParameters") or {}
    # Determine the primary resource (e.g., 'accounts', 'leads', etc.)
    resource = resource_path.strip("/").split("/")[0].lower()
    
    if resource == "accounts":
        try:
            if http_method.upper() == "GET":
                account_id = path_params.get("account_id")
                if account_id:
                    result = account_api.get_by_id(account_id)
                    return ResponseBuilder.build_response(200, result)
                else:
                    result = account_api.get_all()
                    return ResponseBuilder.build_response(200, result)
            
            elif http_method.upper() == "POST":
                body = event.get("body")
                if not body:
                    return ResponseBuilder.build_response(400, {"error": "Missing request body."})
                account_data = json.loads(body)
                result = account_api.create(account_data)
                return ResponseBuilder.build_response(201, result)
            
            elif http_method.upper() == "PUT":
                account_id = path_params.get("account_id")
                if not account_id:
                    return ResponseBuilder.build_response(400, {"error": "Missing account_id in path."})
                body = event.get("body")
                if not body:
                    return ResponseBuilder.build_response(400, {"error": "Missing request body."})
                account_data = json.loads(body)
                result = account_api.update(account_id, account_data)
                return ResponseBuilder.build_response(200, result)
            
            elif http_method.upper() == "DELETE":
                account_id = path_params.get("account_id")
                if not account_id:
                    return ResponseBuilder.build_response(400, {"error": "Missing account_id in path."})
                result = account_api.delete(account_id)
                return ResponseBuilder.build_response(204, result)
            
            else:
                return ResponseBuilder.build_response(405, {"error": "Method Not Allowed."})
        except Exception as e:
            logger.error("Error processing accounts operation: %s", e, exc_info=True)
            return ResponseBuilder.build_response(500, {"error": "Internal Server Error."})
    
    # Fallback for unknown resources
    return ResponseBuilder.build_response(404, {"error": "Resource not found."})
