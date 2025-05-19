
import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


import json
from com.dimcon.synthera_netsuite_integration.controller.lambda_entry_point import lambda_handler

def test_get_leads():
    # Simulated Lambda event for GET method on leads resource.
    event = {
        "httpMethod": "GET",
        "resource": "/leads",
        "pathParameters": {}
    }
    # Dummy context (if needed, you can put attributes here)
    context = {}
    
    response = lambda_handler(event, context)
    print("Response:", json.dumps(response, indent=2))

if __name__ == "__main__":
    test_get_leads()